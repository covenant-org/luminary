from transformers import AutoProcessor, AutoModelForVision2Seq
from PIL import Image
import torch
import numpy as np

model_id = "NVIDIA/vila-1.5-3b" 

processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16
)

model.eval()

def generate_summary_vila(frames):
    if not frames:
        return "No se encontraron frames para analizar."

    # Seleccionar un frame representativo (el del medio)
    selected = frames[len(frames) // 2]
    image = Image.fromarray(selected)

    inputs = processor(images=image, return_tensors="pt").to(model.device)

    with torch.no_grad():
        generated_ids = model.generate(**inputs, max_new_tokens=100)

    summary = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return f"Resumen visual generado por VILA: {summary}"