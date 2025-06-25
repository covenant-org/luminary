from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
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

# Plantilla de chat para LLaMA-2
LLAMA_CHAT_TEMPLATE = """<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{history}
{user_input} [/INST]"""

def initialize_chat_model(model_name="TheBloke/Llama-2-7B-chat-GPTQ"):
    global CHAT_MODEL, CHAT_TOKENIZER
    
    if CHAT_MODEL is not None:
        return CHAT_MODEL, CHAT_TOKENIZER
    
    try:
        logger.info(f"Inicializando modelo de chat: {model_name} en {DEVICE}...")
        
        # Cargar tokenizador y modelo
        CHAT_TOKENIZER = AutoTokenizer.from_pretrained(model_name, use_fast=True)
        
        # Forzar configuración de chat_template si no está presente
        if not hasattr(CHAT_TOKENIZER, "chat_template") or CHAT_TOKENIZER.chat_template is None:
            logger.warning("No se encontró chat_template, usando plantilla personalizada")
            CHAT_TOKENIZER.chat_template = LLAMA_CHAT_TEMPLATE
        
        CHAT_MODEL = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype=torch.float16,
            trust_remote_code=True,
            revision="main"
        )
        
        logger.info(f"Modelo de chat {model_name} cargado exitosamente")
        return CHAT_MODEL, CHAT_TOKENIZER
    
    except Exception as e:
        logger.error(f"Error al cargar modelo de chat: {str(e)}")
        raise

def format_llama_prompt(history, question, context):
    """Formatea el prompt manualmente para LLaMA-2"""
    system_prompt = f"""
    Eres un asistente especializado en análisis de video. Responde preguntas basándote en el siguiente contexto:
    
    CONTEXTO HISTÓRICO:
    {context}
    
    Responde de manera concisa, veraz y profesional en español.
    """
    
    # Construir historial de conversación
    conversation = []
    for user_msg, bot_msg in history:
        conversation.append(f"<s>[INST] {user_msg} [/INST]")
        conversation.append(f"{bot_msg}</s>")
    
    # Unir el historial
    history_text = "\n".join(conversation) if conversation else ""
    
    # Formatear según la plantilla
    return LLAMA_CHAT_TEMPLATE.format(
        system_prompt=system_prompt.strip(),
        history=history_text,
        user_input=question
    )

def generate_chat_response(history, question, context, max_new_tokens=256):
    global CHAT_MODEL, CHAT_TOKENIZER
    
    try:
        # Inicializar modelo si no está cargado
        if CHAT_MODEL is None or CHAT_TOKENIZER is None:
            CHAT_MODEL, CHAT_TOKENIZER = initialize_chat_model()
        
        # Formatear prompt manualmente
        prompt = format_llama_prompt(history, question, context)
        
        # Tokenizar manualmente
        inputs = CHAT_TOKENIZER(
            prompt, 
            return_tensors="pt", 
            add_special_tokens=False
        ).to(DEVICE)
        
        # Crear pipeline para generación
        pipe = pipeline(
            "text-generation",
            model=CHAT_MODEL,
            tokenizer=CHAT_TOKENIZER,
            device_map="auto",
            torch_dtype=torch.float16
        )
        
        # Generar respuesta
        outputs = pipe(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=True,
            temperature=0.7,
            top_p=0.95,
            pad_token_id=CHAT_TOKENIZER.eos_token_id,
            eos_token_id=CHAT_TOKENIZER.eos_token_id,
            return_full_text=False  # Solo devolver la nueva generación
        )
        
        # Extraer y limpiar respuesta
        response = outputs[0]['generated_text'].strip()
        
        # Eliminar posibles tokens sobrantes
        if response.endswith('</s>'):
            response = response[:-4]
        
        return response
    
    except Exception as e:
        logger.error(f"Error en generación de chat: {str(e)}", exc_info=True)
        return f"Error: {str(e)}"
    
    finally:
        # Limpieza de memoria
        torch.cuda.empty_cache()
        gc.collect()
        if 'inputs' in locals():
            del inputs
        if 'pipe' in locals():
            del pipe
        if 'outputs' in locals():
            del outputs