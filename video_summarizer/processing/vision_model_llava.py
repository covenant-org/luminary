from transformers import LlavaNextForConditionalGeneration, LlavaNextProcessor, BitsAndBytesConfig
import torch
from PIL import Image
import logging
import gc

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables globales para mantener el modelo cargado
MODEL = None
PROCESSOR = None
CURRENT_MODEL_SIZE = None  # Para rastrear el tamaño del modelo cargado
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def initialize_llava_model(model_size="7b"):
    global MODEL, PROCESSOR, CURRENT_MODEL_SIZE
    
    # Si ya está cargado el modelo del tamaño solicitado, no hacer nada
    if MODEL is not None and CURRENT_MODEL_SIZE == model_size:
        return MODEL, PROCESSOR
    
    # Si hay un modelo cargado pero de diferente tamaño, liberar memoria
    if MODEL is not None:
        del MODEL
        del PROCESSOR
        gc.collect()
        torch.cuda.empty_cache()
        MODEL = None
        PROCESSOR = None
    
    try:
        logger.info(f"Inicializando modelo LLaVA-{model_size} en {DEVICE}...")
        
        # Identificador del modelo
        model_id = f"llava-hf/llava-v1.6-vicuna-{model_size}-hf"
        
        # Configuración de cuantización
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4"
        )
        
        # Cargar procesador y modelo
        PROCESSOR = LlavaNextProcessor.from_pretrained(model_id, use_fast=True)
        MODEL = LlavaNextForConditionalGeneration.from_pretrained(
            model_id,
            quantization_config=quantization_config,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
        # Configuración adicional
        MODEL.config.use_cache = True
        MODEL.generation_config.pad_token_id = PROCESSOR.tokenizer.eos_token_id
        
        CURRENT_MODEL_SIZE = model_size
        logger.info(f"Modelo LLaVA-{model_size} cargado exitosamente")
        return MODEL, PROCESSOR
    
    except Exception as e:
        logger.error(f"Error al cargar modelo LLaVA: {str(e)}")
        raise

def generate_summary_llava(frames, custom_prompt=None, model_size="7b", generation_params=None):
    global MODEL, PROCESSOR, CURRENT_MODEL_SIZE
    
    if not frames or all(f is None for f in frames):
        return "No se encontraron frames válidos para analizar."
    
    try:
        # Establecer parámetros predeterminados si no se proporcionan
        if generation_params is None:
            generation_params = {
                'max_tokens': 300,
                'temperature': 0.6,
                'top_p': 0.95,
                'num_beams': 2,
                'repetition_penalty': 1.2,
                'length_penalty': 1.3
            }
        
        # Monitorear memoria antes de procesar
        logger.info(f"VRAM antes: {torch.cuda.memory_allocated()/1024**3:.2f} GB")

        # Inicializar modelo si no está cargado o si el tamaño ha cambiado
        if MODEL is None or PROCESSOR is None or CURRENT_MODEL_SIZE != model_size:
            MODEL, PROCESSOR = initialize_llava_model(model_size)
        
        # Seleccionar el último frame válido
        valid_frames = [f for f in frames if f is not None]
        if not valid_frames:
            return "No hay frames válidos para análisis"
            
        selected_frame = valid_frames[-1]
        image = Image.fromarray(selected_frame)
        
        # Crear prompt personalizado o usar default
        if custom_prompt:
            prompt = f"USER: <image>\n{custom_prompt}\nASSISTANT:"
        else:
            prompt = "USER: <image>\nDescribe en detalle la escena completa incluyendo: personas (edad estimada, ropa, acciones), objetos, entorno, colores, y cualquier elemento relevante. Responde en español con al menos 200 palabras.\nASSISTANT:"
        
        # Procesar inputs
        inputs = PROCESSOR(
            text=prompt,
            images=image,
            return_tensors="pt"
        ).to(DEVICE)
        
        # Generar respuesta con parámetros personalizados
        output = MODEL.generate(
            **inputs,
            max_new_tokens=generation_params['max_tokens'],
            temperature=generation_params['temperature'],
            top_p=generation_params['top_p'],
            do_sample=True,
            num_beams=generation_params['num_beams'],
            repetition_penalty=generation_params['repetition_penalty'],
            length_penalty=generation_params['length_penalty']
        )
        
        # Decodificar y limpiar respuesta
        full_response = PROCESSOR.decode(output[0], skip_special_tokens=True)
        response = full_response.split("ASSISTANT:")[-1].strip()

        # Monitorear memoria después
        logger.info(f"VRAM después: {torch.cuda.memory_allocated()/1024**3:.2f} GB")
        
        return f"Resumen visual (LLaVA): {response}"
    
    except Exception as e:
        logger.error(f"Error en generación de resumen: {str(e)}", exc_info=True)
        return f"Error: {str(e)}"
    
    finally:
        # Limpieza intensiva
        torch.cuda.empty_cache()
        gc.collect()
        if 'inputs' in locals():
            del inputs
        if 'output' in locals():
            del output
        if 'image' in locals():
            del image
        torch.cuda.ipc_collect()
