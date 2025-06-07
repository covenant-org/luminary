import subprocess
import numpy as np
import cv2

rtsp_url = "rtsp://admin:L2F4FD58@192.168.10.90:554/cam/realmonitor?channel=1&subtype=0"
width, height = 1920, 1080
frame_size = width * height * 3  # bgr24

command = [
		'ffmpeg',
		'-rtsp_transport', 'tcp',   # fuerza TCP para RTSP
		'-i', rtsp_url,             # sin comillas extras
		'-f', 'rawvideo',
		'-pix_fmt', 'bgr24',
		'-'
]

process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

while True:
		raw_frame = process.stdout.read(frame_size)
		if len(raw_frame) != frame_size:
				print("No se pudo leer el frame completo (stream terminado o error)")
				break
		frame = np.frombuffer(raw_frame, np.uint8).reshape((height, width, 3))
		cv2.imshow('Stream RTSP', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
				break

process.terminate()
cv2.destroyAllWindows()

# Opcional: leer errores ffmpeg
stderr_output = process.stderr.read().decode()
print(stderr_output)
