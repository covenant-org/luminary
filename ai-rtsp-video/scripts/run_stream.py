import cv2
import os
import sys
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.rtsp_stream import RTSPStreamFFmpeg
from app.processor import FrameProcessor
from app.zone_detector import ZoneDetector

def box_in_zone(box, zone):
		# box y zone formato (x1, y1, x2, y2)
		bx1, by1, bx2, by2 = box
		zx1, zy1, zx2, zy2 = zone
		# Verifica si la caja está dentro (total o parcialmente) de la zona
		return not (bx2 < zx1 or bx1 > zx2 or by2 < zy1 or by1 > zy2)

def main():
		dotenv_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '.env')
		load_dotenv(dotenv_path=dotenv_path)

		rtsp_url = os.getenv("RTSP_URL", "")
		print("RTSP URL:", rtsp_url)
		
		stream = RTSPStreamFFmpeg(rtsp_url)
		processor = FrameProcessor()
		zones = [(100, 100, 300, 300)]
		zone_detector = ZoneDetector(zones=zones)

		while True:
				frame = stream.read_frame()
				results = processor.detect(frame)
				frame = zone_detector.highlight_zones(frame)
				
				# Hacer una copia para evitar error readonly
				frame = frame.copy()

				for box in results.boxes.xyxy:
						x1, y1, x2, y2 = map(int, box)
						# Color y grosor por defecto
						color = (255, 0, 0)
						thickness = 2

						# Cambiar color y grosor si está en zona
						for zone in zones:
								if box_in_zone((x1, y1, x2, y2), zone):
										color = (0, 255, 0)
										thickness = 3
										break

						cv2.rectangle(frame, (x1, y1), (x2, y2), color, thickness)

				cv2.imshow("RTSP Stream", frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
						break

		stream.release()
		cv2.destroyAllWindows()

if __name__ == "__main__":
		main()
