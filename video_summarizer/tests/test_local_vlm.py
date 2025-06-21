import subprocess
import sys
import os
import torch
from PIL import Image
import numpy as np
from tqdm import tqdm

# Verificar e instalar dependencias faltantes
try:
    import sentencepiece
except ImportError:
    print("Instalando sentencepiece...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "sentencepiece"])

try:
    import decord
except ImportError:
    print("Instalando decord...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "decord"])

try:
    import google.protobuf
except ImportError:
    print("Instalando protobuf...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "protobuf"])

# Ahora importamos el resto de bibliotecas
from transformers import LlavaNextForConditionalGeneration, LlavaNextProcessor, BitsAndBytesConfig

# Configuración inicial - USAR RUTA ABSOLUTA O VERIFICAR EXISTENCIA
MODEL_ID = "llava-hf/llava-v1.6-vicuna-7b-hf"
VIDEO_PATH = os.path.abspath("videoplayback.mp4")  # Ruta absoluta                 
OUTPUT_FILE = "analisis_video.txt" 
FRAME_RATE = 1 
PROMPT = "USER: <image>\nDescribe escena, objetos principales y acciones visibles. Responde en español.\nASSISTANT:"

def extract_video_frames(video_path, frame_rate=1):
    """Extrae frames del video usando decord"""
    import decord
    
    # Verificar si el archivo existe
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"Archivo de video no encontrado: {video_path}")
    
    try:
        vr = decord.VideoReader(video_path)
    except Exception as e:
        print(f"Error al abrir el video: {str(e)}")
        print("Posibles soluciones:")
        print("1. Asegúrate de que el archivo existe y es un video válido")
        print("2. Instala codecs de video: sudo apt install ffmpeg libavcodec-extra")
        raise
    
    total_frames = len(vr)
    frame_step = max(1, int(vr.get_avg_fps() / frame_rate))
    
    frames = []
    timestamps = []
    
    for i in tqdm(range(0, total_frames, frame_step), desc="Extrayendo frames"):
        frame = vr[i].asnumpy()
        # Reducir resolución para mejorar rendimiento
        img = Image.fromarray(frame).resize((640, 360))
        frames.append(img)
        timestamps.append(i / vr.get_avg_fps())
    
    return frames, timestamps

def initialize_model(model_id):
    """Carga el modelo con optimización"""
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_quant_type="nf4"
    )
    
    model = LlavaNextForConditionalGeneration.from_pretrained(
        model_id,
        torch_dtype=torch.float16,
        device_map="auto",
        quantization_config=quantization_config
    )
    
    # Cargar el procesador con use_fast=True para evitar advertencias
    processor = LlavaNextProcessor.from_pretrained(
        model_id,
        use_fast=True  # Usar tokenizador rápido
    )
    
    model.config.use_cache = True
    model.generation_config.pad_token_id = processor.tokenizer.eos_token_id
    
    return model, processor

def analyze_frames(frames, timestamps, model, processor):
    """Procesa los frames con el modelo VLM"""
    results = []
    
    for i, (frame, timestamp) in tqdm(enumerate(zip(frames, timestamps)), total=len(frames), desc="Analizando video"):
        inputs = processor(
            text=PROMPT,
            images=frame,
            return_tensors="pt"
        ).to(model.device)
        
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.3,
            top_p=0.9,
            do_sample=True
        )
        
        description = processor.decode(output[0], skip_special_tokens=True)
        description = description.split("ASSISTANT:")[-1].strip()
        
        results.append({
            "frame": i,
            "timestamp": f"{int(timestamp//60)}m:{int(timestamp%60)}s",
            "description": description
        })
        
        # Limpieza de memoria
        del inputs
        del output
        torch.cuda.empty_cache()
    
    return results

def save_results(results, output_file):
    """Guarda los resultados en un archivo"""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("Análisis de video - Modelo LLaVA 1.6\n")
        f.write("=====================================\n\n")
        
        for res in results:
            f.write(f"[Tiempo: {res['timestamp']} | Frame: {res['frame']}]\n")
            f.write(f"{res['description']}\n")
            f.write("-" * 80 + "\n")

def get_gpu_utilization():
    """Obtiene el uso de GPU"""
    try:
        output = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"],
            encoding="utf-8"
        )
        return output.strip()
    except:
        return "No disponible"

if __name__ == "__main__":
    # Verificar GPU
    try:
        gpu_info = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader"],
            encoding="utf-8"
        )
        print(f"GPU detectada:\n{gpu_info}")
    except:
        print("Advertencia: No se pudo obtener información de GPU")
    
    # Verificar existencia del video
    print(f"\nBuscando video: {VIDEO_PATH}")
    if not os.path.isfile(VIDEO_PATH):
        print("\nERROR: Archivo de video no encontrado")
        print("Posibles soluciones:")
        print(f"1. Coloca el video en: {os.getcwd()}")
        print(f"2. Actualiza la variable VIDEO_PATH en el script")
        print(f"3. Ejecuta desde el directorio correcto")
        exit(1)
    
    print(f"\nInicializando modelo {MODEL_ID}...")
    model, processor = initialize_model(MODEL_ID)
    
    print("\nExtrayendo frames del video...")
    try:
        frames, timestamps = extract_video_frames(VIDEO_PATH, FRAME_RATE)
    except Exception as e:
        print(f"Error al procesar video: {str(e)}")
        print("Asegúrate de tener los codecs necesarios instalados:")
        print("sudo apt install ffmpeg libavcodec-extra")
        exit(1)
    
    print(f"\nProcesando {len(frames)} frames con VLM...")
    results = analyze_frames(frames, timestamps, model, processor)
    
    print("\nGuardando resultados...")
    save_results(results, OUTPUT_FILE)
    
    print(f"\n¡Análisis completo! Resultados guardados en: {OUTPUT_FILE}")
    print(f"Uso final GPU: {get_gpu_utilization()}")