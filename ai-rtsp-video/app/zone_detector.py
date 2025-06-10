import cv2

class ZoneDetector:
		def __init__(self, zones):
				self.zones = zones

		def highlight_zones(self, frame):
				# Dibuja rectángulos verdes en las zonas de interés
				frame_out = frame.copy()
				for (x1, y1, x2, y2) in self.zones:
						cv2.rectangle(frame_out, (x1, y1), (x2, y2), (0, 255, 0), 2)
				return frame_out
