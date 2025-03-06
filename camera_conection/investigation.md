# Lógica conexión cámaras con nube


## **Configuración de cámara**

- Acceder a la interfaz web de la cámara

- Asignar una ip estática

- Habilitar ONVIF

- Configurar credenciales

- Configurar resolución, fps, bitrate, formato de compresión, etc. 

- Testear cámaras con ONVIF Device Manager


## **Configuración de NVR**

- NVR en la misma red que las cámaras

- Configurar con mismas credenciales que cámaras

- Usar auto-discovery para encontrar cámaras con ONVIF (agregar ip manualmente de ser necesario)


## **Configuración de grabaciones**

- Configurar grabación contínua o provocada por una acción(ej detección de movimiento) o cada cierto tiempo

- Dividir las grabaciones en segmentos más pequeños (5 min - 10 min) con herramientas como FFmpeg. 


## **Configuración de AWS**

- Crear bucket en el servicio de S3

- Configurar permisos de acceso

- AWS Transfer Family soporta FTP, FTPS y SFTP para integrar directamente con s3

- Configurar servidor FTP con AWS Transfer Family

- Guardar archivos en bucked de AWS


## **Configuración de NVR - AWS**

- Acceder a interfaz administrativa de NVR

- Ingresar dirección del servidor FTP proveída por AWS Transfer Family (si disponible)

- Configurar script o AWS CLI en dispositivo externo para hacer la carga

- Ingresar credenciales para autenticación 

- Específicar directorio destino dependiendo de la estructura

- Testear conexiones 

## **Conexión con Label Studio**

- Llamar a una función (ej AWS Lambda) cuando un video se suba

- Generar URL para cada archivo de video

- En la llamada a la función hacer un HTTP POST a Label Studio API para crear una tarea

- Incluir URL, metadata

# **Configuración de Label Studio**

- Configurar el projecto para manejar videos y definir ripo de etiquetado

- Unir resultado (ej archivo JSON) al dataset


# Conceptos


## **RTSP**

Real Time Streaming Protocol, protocolo de control de un servidor de transmisión de medios (video) de manera remota. Se usa para establecer y controlar sesiones de medios entre puntos finales. Los clientes de los servidores de medios emiten comandos como *reproducir, grabar *y *pausar*, para facilitar el control en tiempo real de la transmisión desde el servidor a un cliente. 


## **ONVIF**

Open Network Video Interface Forum, estándar de industria que especifica interfaces comunes para productos de seguridad basadas en ip, como cámaras


## **NVR**

Network Video Recorder, dispositivo especializado diseñado para recibir, grabar y manejar transmisiones de video digitales desde cámaras IP, el NVR graba el video que ya está en formato digital, normalmente transmitido sobre Ethernet. 

Pueden recibir captura de video directamente de cámaras IP, usan cables de conexión estándar, soportan alta resolución, acceso remoto e integración con softwares de manejo de video


## **FTP Upload**

File Transfer Protocol, protocolo que permite transferir archivos directamente de un dispositivo a otro, las conexiones tienen una relación de cliente y servidor, en el servidor se aloja el contenido y luego te conectas a él como cliente. Los datos se envían a través de los puertos 20 y 21


## **HTTP Upload**

Usa el Hypertext Transfer Protocol, normalmente en métodos como HTTP POST para mandar archivos a un servidor web o servicio en la nube, puede simplificar la integración con APIs basadas en web y servicios.

# Fuentes

- https://www.dvraid.com/guide/network-video-recorder-complete-setup-guide/#:~:text=Here%E2%80%99s%20a%20simple%20step-by-step%20process%3A%201%201.Unbox%20the,This%20allows%20you%20to%20access%20the%20NVR%20remotely.

- [https://chatgpt.com/share/67c8574d-e450-800c-837a-db9e1f3935ef](https://chatgpt.com/share/67c8574d-e450-800c-837a-db9e1f3935ef)

- https://www.videoexpertsgroup.com/glossary/how-to-connect-camera-to-onvif#:~:text=How%20to%20Connect%20an%20IP%20Camera%20via%20ONVIF%3A,Step%205%3A%20Test%20and%20Monitor%20the%20Connection%20

- https://aws.amazon.com/es/blogs/storage/collecting-archiving-and-retrieving-surveillance-footage-with-aws/

- https://aws.amazon.com/es/blogs/iot/build-a-cloud-gateway-to-ingest-rtsp-video-to-amazon-kinesis-video-streams/

- http://labelstud.io.s3-website-us-east-1.amazonaws.com/guide/storage.html#Amazon-S3

