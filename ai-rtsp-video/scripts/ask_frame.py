import cv2
from app.vqa import VQASystem

vqa = VQASystem()
frame = cv2.imread("data/raw/frame.jpg")
question = "¿Cuántas personas hay?"
respuesta = vqa.ask(frame, question)
print("Respuesta:", respuesta)