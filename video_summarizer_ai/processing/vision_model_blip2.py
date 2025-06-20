from transformers import Blip2Processor, Blip2ForConditionalGeneration
from PIL import Image
import torch
import numpy as np

# Cargar modelo BLIP-2
device = "cuda" if torch.cuda.is_available() else "cpu"
processor = Blip2Processor.from_pretrained("Salesforce/blip2-opt-2.7b")
model = Blip2ForConditionalGeneration.from_pretrained("Salesforce/blip2-opt-2.7b", device_map="auto").to(device)

def generate_summary_blip2(frames):
    if not frames:
        return "No se encontraron frames para analizar."

    # Usar solo los últimos frames más representativos (ej: el del medio)
    selected = frames[len(frames)//2]
    image = Image.fromarray(selected)

    inputs = processor(images=image, return_tensors="pt").to(device)
    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=50)
    summary = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

    return f"Resumen visual generado: {summary}"