import subprocess

rtsp_url = "rtsp://admin:L2F4FD58@192.168.10.90:554/cam/realmonitor?channel=1&subtype=0"

# Comando para ffplay con transporte TCP
command = [
		"ffplay",
		"-rtsp_transport", "tcp",
		rtsp_url
]

# Ejecutar ffplay y mantener la ventana abierta hasta que el usuario la cierre
process = subprocess.Popen(command)

# Opcional: esperar a que termine ffplay antes de continuar con Python
process.wait()
