from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import time

# Configuración corregida (usando un modelo chat especializado)
model_name = "TheBloke/Llama-2-7B-chat-GPTQ"  # Modelo optimizado para diálogo

# Verificar GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Usando dispositivo: {device}")
print(f"Memoria GPU disponible: {torch.cuda.get_device_properties(0).total_memory/1e9:.2f} GB")

# Cargar modelo con configuración adecuada
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True,
    revision="main"
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    torch_dtype=torch.float16
)

def generate_response(prompt):
    # Formatear prompt según requerimientos de LLaMA 2
    formatted_prompt = f"""<s>[INST] <<SYS>>
Eres un asistente científico experto en física relativista.
Responde de manera clara y concisa en español.
<</SYS>>

{prompt} [/INST]"""
    
    start_time = time.time()
    
    outputs = pipe(
        formatted_prompt,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.eos_token_id,
        num_return_sequences=1
    )
    
    generation_time = time.time() - start_time
    full_response = outputs[0]['generated_text']
    
    response = full_response.split('[/INST]')[-1].strip()
    tokens = len(tokenizer.encode(response))
    
    return response, generation_time, tokens

prompt = "Explica la teoría de la relatividad en términos simples:"
print(f"\n\033[1mPrompt:\033[0m {prompt}")

response, time_taken, tokens = generate_response(prompt)

print(f"\n\033[1mRespuesta:\033[0m {response}")
print(f"\n\033[92mTokens generados: {tokens}")
print(f"Tiempo total: {time_taken:.2f}s")
print(f"Velocidad: {tokens/time_taken:.2f} tokens/segundo\033[0m")