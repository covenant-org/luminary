import cv2
import numpy as np

class MotionEngine:
    def __init__(self, frame_shape, mask_path=None):
        self.height, self.width = frame_shape[:2]
        self.avg_frame = None
        

        if mask_path:
            self.mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
            self.mask = cv2.resize(self.mask, (self.width, self.height))
        else:
            self.mask = np.full((self.height, self.width), 255, dtype="uint8")

    def process(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        gray = cv2.bitwise_and(gray, gray, mask=self.mask)

        if self.avg_frame is None:
            self.avg_frame = gray.copy().astype("float")
            return False, []

        cv2.accumulateWeighted(gray, self.avg_frame, 0.5)
        frame_delta = cv2.absdiff(gray, cv2.convertScaleAbs(self.avg_frame))
        
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        motion_boxes = []
        for c in contours:
            if cv2.contourArea(c) < 500:
                continue
            motion_boxes.append(cv2.boundingRect(c))
            
        return len(motion_boxes) > 0, motion_boxes