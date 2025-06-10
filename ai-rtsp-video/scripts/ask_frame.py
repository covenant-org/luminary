import os
import cv2
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.vqa import VQASystem

vqa = VQASystem()
frame = cv2.imread("data/raw/frame.jpg")
question = "¿Cuántas personas hay?"
respuesta = vqa.ask(frame, question)
print("Respuesta:", respuesta)