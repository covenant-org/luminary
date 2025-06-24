from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
import logging
import gc

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Variables globales para el modelo de chat
CHAT_MODEL = None
CHAT_TOKENIZER = None
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

def initialize_chat_model(model_name="HuggingFaceH4/zephyr-7b-beta"):
    global CHAT_MODEL, CHAT_TOKENIZER
    
    if CHAT_MODEL is not None:
        return CHAT_MODEL, CHAT_TOKENIZER
    
    try:
        logger.info(f"Inicializando modelo de chat: {model_name} en {DEVICE}...")
        
        # Configuración de cuantización
        quantization_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.float16,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True
        )
        
        # Cargar tokenizador y modelo
        CHAT_TOKENIZER = AutoTokenizer.from_pretrained(model_name)
        CHAT_MODEL = AutoModelForCausalLM.from_pretrained(
            model_name,
            quantization_config=quantization_config,
            torch_dtype=torch.float16,
            device_map="auto"
        )
        
        logger.info(f"Modelo de chat {model_name} cargado exitosamente")
        return CHAT_MODEL, CHAT_TOKENIZER
    
    except Exception as e:
        logger.error(f"Error al cargar modelo de chat: {str(e)}")
        raise

def generate_chat_response(history, question, context, max_new_tokens=256):
    global CHAT_MODEL, CHAT_TOKENIZER
    
    try:
        # Inicializar modelo si no está cargado
        if CHAT_MODEL is None or CHAT_TOKENIZER is None:
            CHAT_MODEL, CHAT_TOKENIZER = initialize_chat_model()
        
        # Crear prompt con contexto histórico
        system_prompt = f"""
        Eres un asistente especializado en análisis de video. Responde preguntas basándote en el siguiente contexto:
        
        CONTEXTO HISTÓRICO:
        {context}
        
        Responde de manera concisa, veraz y profesional en español.
        """
        
        # Construir historial de conversación
        messages = [
            {"role": "system", "content": system_prompt}
        ]
        
        # Añadir historial de chat
        for user_msg, bot_msg in history:
            messages.append({"role": "user", "content": user_msg})
            messages.append({"role": "assistant", "content": bot_msg})
        
        # Añadir nueva pregunta
        messages.append({"role": "user", "content": question})
        
        # Formatear para el modelo
        prompt = CHAT_TOKENIZER.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        
        # Tokenizar
        inputs = CHAT_TOKENIZER(prompt, return_tensors="pt").to(DEVICE)
        
        # Generar respuesta
        outputs = CHAT_MODEL.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            pad_token_id=CHAT_TOKENIZER.eos_token_id
        )
        
        # Decodificar respuesta
        response = CHAT_TOKENIZER.decode(
            outputs[0][inputs.input_ids.shape[1]:], 
            skip_special_tokens=True
        )
        
        return response.strip()
    
    except Exception as e:
        logger.error(f"Error en generación de chat: {str(e)}", exc_info=True)
        return f"Error: {str(e)}"
    
    finally:
        # Limpieza de memoria
        torch.cuda.empty_cache()
        gc.collect()
        if 'inputs' in locals():
            del inputs
        if 'outputs' in locals():
            del outputs