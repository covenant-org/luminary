import cv2

class RTSPStream:
    def __init__(self, url):
        self.url = url
        self.cap = cv2.VideoCapture(self.url)

    def read_frames(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            yield frame

    def release(self):
        if self.cap.isOpened():
            self.cap.release()
