import subprocess
import numpy as np
import cv2

class FFmpegStream:
    def __init__(self, url):
        self.url = url
        self.width = 640
        self.height = 480
        self.proc = subprocess.Popen(
            [
                'ffmpeg',
                '-hwaccel', 'auto',
                '-i', self.url,
                '-f', 'rawvideo',
                '-pix_fmt', 'bgr24',
                '-vf', f'scale={self.width}:{self.height}',
                '-'
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

    def read_frame(self):
        raw_size = self.width * self.height * 3 
        raw_frame = self.proc.stdout.read(raw_size)
        if len(raw_frame) != raw_size:
            return None
        frame = np.frombuffer(raw_frame, np.uint8).reshape((self.height, self.width, 3))
        return frame

    def close(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            self.proc.wait()
