import cv2

class ZoneDetector:
    def __init__(self, zones):
        self.zones = zones

    def highlight_zones(self, frame):
        # Crear una copia para que sea modificable
        modifiable_frame = frame.copy()

        for (x1, y1, x2, y2) in self.zones:
            cv2.rectangle(modifiable_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        return modifiable_frame
