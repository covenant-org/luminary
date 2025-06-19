import torch
import clip
from PIL import Image
import numpy as np
import torchvision.transforms as transforms

# Cargar modelo CLIP (usa ViT-B/32 por defecto)
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

DEFAULT_PROMPTS = [
    "una persona",
    "un auto",
    "una calle",
    "una multitud",
    "una pelea",
    "una casa",
    "una oficina",
    "una bicicleta",
    "una motocicleta",
    "una cámara",
    "una conversación",
    "una escena vacía"
]

def analyze_frames(frames, prompts=DEFAULT_PROMPTS):
    if not frames:
        return "No se encontraron frames para analizar."

    images = [Image.fromarray(frame) for frame in frames]
    image_tensors = torch.stack([preprocess(img) for img in images]).to(device)

    with torch.no_grad():
        text_tokens = clip.tokenize(prompts).to(device)
        image_features = model.encode_image(image_tensors)
        text_features = model.encode_text(text_tokens)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        text_features = text_features / text_features.norm(dim=-1, keepdim=True)

        similarities = (image_features @ text_features.T).cpu().numpy()

    # Promediar similitud por clase
    avg_sim = similarities.mean(axis=0)
    top_idx = np.argmax(avg_sim)
    top_prompt = prompts[top_idx]
    score = avg_sim[top_idx]

    return f"Resumen visual: Se detecta principalmente '{top_prompt}' (confianza {score:.2f})"