import subprocess
import numpy as np
import threading

class RTSPStreamFFmpeg:
		def __init__(self, rtsp_url, width=1920, height=1080):
				self.rtsp_url = rtsp_url
				self.width = width
				self.height = height
				self.frame_size = self.width * self.height * 3  # bgr24: 3 bytes per pixel

				self.command = [
						'ffmpeg',
						'-rtsp_transport', 'tcp',
						'-i', self.rtsp_url,
						'-f', 'rawvideo',
						'-pix_fmt', 'bgr24',
						'-vf', f'scale={self.width}:{self.height}',
						'-'
				]

				self.process = subprocess.Popen(
						self.command,
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE,
						bufsize=10**8
				)

				threading.Thread(target=self._print_stderr, daemon=True).start()

		def _print_stderr(self):
				for line in iter(self.process.stderr.readline, b''):
						print("[ffmpeg]", line.decode().strip())

		def read_frame(self):
				raw_frame = b''
				while len(raw_frame) < self.frame_size:
						chunk = self.process.stdout.read(self.frame_size - len(raw_frame))
						if not chunk:
								print("[RTSPStreamFFmpeg] Incomplete frame or stream closed. Skipping frame.")
								return None
						raw_frame += chunk
				frame = np.frombuffer(raw_frame, np.uint8).reshape((self.height, self.width, 3))
				return frame

		def release(self):
				self.process.terminate()
				self.process.wait()
