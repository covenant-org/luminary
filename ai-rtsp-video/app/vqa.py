from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

class VQASystem:
		def __init__(self):
				self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
				self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-vqa-base")

		def ask(self, frame, question):
				image = Image.fromarray(frame[..., ::-1])  # BGR to RGB
				inputs = self.processor(image, question, return_tensors="pt")
				out = self.model.generate(**inputs)
				return self.processor.decode(out[0], skip_special_tokens=True)