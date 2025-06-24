from llama_cpp import Llama
import time

# Configuración del modelo
model_path = "./llama-2-7b.Q4_K_M.gguf" 
n_gpu_layers = 40
n_ctx = 4096 

llm = Llama(
    model_path=model_path,
    n_gpu_layers=n_gpu_layers,
    n_ctx=n_ctx,
    n_threads=8,
    seed=42,
    verbose=False
)

def run_inference(prompt, max_tokens=256):
    start_time = time.time()
    
    output = llm(
        prompt,
        max_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        echo=False,
        stream=False
    )
    
    generation_time = time.time() - start_time
    tokens_generated = len(output['choices'][0]['text'].split())
    
    return output, generation_time, tokens_generated

prompts = [
    "Explica la teoría de la relatividad en términos simples:",
    "Traduce al francés: 'El arte de programar requiere lógica y creatividad'",
    "Resume el argumento de 'Cien años de soledad':"
]


for i, prompt in enumerate(prompts):
    print(f"\n\033[1mPrompt {i+1}:\033[0m {prompt}")
    output, time, tokens = run_inference(prompt)
    
    print(f"\n\033[1mRespuesta:\033[0m")
    print(output['choices'][0]['text'].strip())
    
    print(f"\n\033[92mTokens generados: {tokens}")
    print(f"Tiempo total: {time:.2f}s")
    print(f"Tokens/segundo: {tokens/time:.2f}\033[0m")


print("\n\033[1mEjecutando benchmark...\033[0m")
_, time, tokens = run_inference(
    "Repite: 'Benchmark' " * 10,
    max_tokens=512
)
print(f"\033[92mRendimiento sostenido: {tokens/time:.2f} tokens/segundo\033[0m")