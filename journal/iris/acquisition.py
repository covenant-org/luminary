import subprocess
import numpy as np

class CameraAcquisition:
    def __init__(self, rtsp_url, width=1080, height=720, fps=5):
        self.rtsp_url = rtsp_url
        self.width = width
        self.height = height
        self.fps = fps
        self.frame_size = width * height * 3  # 3 bytes per pixel (BGR)
        self.process = None

        # The FFmpeg command:
        # -rtsp_transport tcp: Prevents "smearing" by using reliable packets
        # -r: Sets the frame rate (Frigate uses 5fps for detection usually)
        # -vf scale: Resizes the frame immediately
        command = [
            'ffmpeg',
            '-rtsp_transport', 'tcp',
            '-i', self.rtsp_url,
            '-vf', f'scale={self.width}:{self.height}',
            '-r', str(self.fps),
            '-f', 'rawvideo',
            '-pix_fmt', 'bgr24',
            '-'
        ]
        
        # Launch FFmpeg as a background process
        self.process = subprocess.Popen(
            command, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.DEVNULL, # Hide FFmpeg logs for now
            bufsize=10**8
        )

        print(f"[*] Started acquisition for: {self.rtsp_url}")        

    # def get_frame(self):
    #     # Read exactly one frame's worth of bytes from the pipe
    #     raw_frame = self.process.stdout.read(self.frame_size)
        
    #     if len(raw_frame) != self.frame_size:
    #         return None

    #     # Convert raw bytes into a 3D NumPy array [height, width, channels]
    #     frame = np.frombuffer(raw_frame, dtype='uint8').reshape((self.height, self.width, 3))
    #     return frame
    

    def get_frame(self):
        raw_frame = self.process.stdout.read(self.frame_size)
        
        if len(raw_frame) != self.frame_size:
            return None

        # Add .copy() at the end here
        frame = np.frombuffer(raw_frame, dtype='uint8').reshape((self.height, self.width, 3)).copy()
        return frame

    def stop(self):
        if self.process:
            self.process.terminate()