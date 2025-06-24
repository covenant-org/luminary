from transformers import LlavaNextForConditionalGeneration, LlavaNextProcessor, BitsAndBytesConfig
import torch
from PIL import Image
import logging
import gc
import os
import subprocess

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables globales para mantener el modelo cargado
MODEL = None
PROCESSOR = None
CURRENT_MODEL_SIZE = None  # Para rastrear el tamaño del modelo cargado
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def unload_model():
    """Libera memoria de GPU de forma más agresiva"""
    global MODEL, PROCESSOR, CURRENT_MODEL_SIZE
    
    if MODEL is not None:
        del MODEL
    if PROCESSOR is not None:
        del PROCESSOR
    
    MODEL = None
    PROCESSOR = None
    CURRENT_MODEL_SIZE = None
    
    gc.collect()
    torch.cuda.empty_cache()
    
    # Forzar limpieza adicional
    if torch.cuda.is_available():
        torch.cuda.synchronize()
        for i in range(torch.cuda.device_count()):
            torch.cuda.reset_peak_memory_stats(i)
    
    logger.info("Memoria GPU liberada completamente")

def initialize_llava_model(model_size="7b"):
    global MODEL, PROCESSOR, CURRENT_MODEL_SIZE
    
    # Si ya está cargado el modelo del tamaño solicitado, no hacer nada
    if MODEL is not None and CURRENT_MODEL_SIZE == model_size:
        return MODEL, PROCESSOR
    
    # Si hay un modelo cargado pero de diferente tamaño, liberar memoria
    if MODEL is not None:
        unload_model()
    
    try:
        logger.info(f"Inicializando modelo LLaVA-{model_size} en {DEVICE}...")
        
        # Identificador del modelo
        model_id = f"llava-hf/llava-v1.6-vicuna-{model_size}-hf"
        
        # Configuración de cuantización mejorada
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True  # Mejor compresión
        )
        
        # Cargar procesador y modelo
        PROCESSOR = LlavaNextProcessor.from_pretrained(model_id, use_fast=True)
        
        MODEL = LlavaNextForConditionalGeneration.from_pretrained(
            model_id,
            quantization_config=quantization_config,
            torch_dtype=torch.float16,
            device_map="auto",
            low_cpu_mem_usage=True  # Reduce uso de RAM durante carga
        )
        
        # Configuración adicional para ahorro de memoria
        MODEL.config.use_cache = True
        MODEL.generation_config.pad_token_id = PROCESSOR.tokenizer.eos_token_id
        MODEL.eval()  # Modo evaluación para menos consumo
        
        CURRENT_MODEL_SIZE = model_size
        
        # Reportar uso de memoria
        if torch.cuda.is_available():
            vram_used = torch.cuda.memory_allocated() / 1024**3
            logger.info(f"Modelo LLaVA-{model_size} cargado | VRAM usada: {vram_used:.2f} GB")
        else:
            logger.info(f"Modelo LLaVA-{model_size} cargado en CPU")
            
        return MODEL, PROCESSOR
    
    except Exception as e:
        logger.error(f"Error al cargar modelo LLaVA: {str(e)}")
        unload_model()  # Limpiar en caso de error
        raise

def generate_summary_llava(frames, custom_prompt=None, model_size="7b", generation_params=None):
    global MODEL, PROCESSOR, CURRENT_MODEL_SIZE
    
    if not frames or all(f is None for f in frames):
        return "No se encontraron frames válidos para analizar."
    
    try:
        # Verificar memoria disponible antes de cargar modelo
        if torch.cuda.is_available():
            total_vram = torch.cuda.get_device_properties(0).total_memory
            used_vram = torch.cuda.memory_allocated()
            free_vram = total_vram - used_vram
            
            # Requerimientos mínimos estimados
            min_7b = 6 * 1024**3  # 6 GB para 7B
            min_13b = 12 * 1024**3  # 12 GB para 13B
            
            if model_size == "13b" and free_vram < min_13b:
                return f"Error: VRAM insuficiente para modelo 13B. Necesita {min_13b/1024**3:.1f}GB, tiene {free_vram/1024**3:.1f}GB libres"
            elif free_vram < min_7b:
                return f"Error: VRAM insuficiente. Necesita al menos {min_7b/1024**3:.1f}GB, tiene {free_vram/1024**3:.1f}GB libres"
        
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
        if torch.cuda.is_available():
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
        if torch.cuda.is_available():
            logger.info(f"VRAM después: {torch.cuda.memory_allocated()/1024**3:.2f} GB")
        
        return f"Resumen visual (LLaVA): {response}"
    
    except torch.cuda.OutOfMemoryError as oom:
        logger.error(f"Error OOM en generación de resumen: {str(oom)}")
        unload_model()
        return f"Error: Memoria GPU agotada. Intente reducir el tamaño del modelo o los parámetros"
    
    except Exception as e:
        logger.error(f"Error en generación de resumen: {str(e)}", exc_info=True)
        return f"Error: {str(e)}"
    
    finally:
        # Limpieza intensiva
        torch.cuda.empty_cache()
        gc.collect()
        
        # Liberar recursos específicos
        for var in ['inputs', 'output', 'image']:
            if var in locals():
                del locals()[var]
        
        if torch.cuda.is_available():
            torch.cuda.ipc_collect()