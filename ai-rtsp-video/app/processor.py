from ultralytics import YOLO
import supervision as sv

class FrameProcessor:
		def __init__(self, model_path='yolov8n.pt'):
				self.model = YOLO(model_path)

		def detect(self, frame):
				results = self.model(frame)
				return results[0]