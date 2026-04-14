# NoeRos22

## 09/04/2026

Script de adquisición del stream, decodificación y muestreo de datos completado, testeado y funcional con ffmpeg. 
En desarrollo: detección de movimiento.

## 08/04/2026

Setup del devcontainer y revisión del estado actual de Vergil.

Investigación del pipeline de video de Frigate (issue #37)

- **Adquisición del feed** — entrada desde cámaras RTSP u otras fuentes, generando feeds principal y secundario.
- **Decodificación y muestreo** — el sub-feed se decodifica, escala y reduce a ~5 FPS.
- **Detección de movimiento** — se comparan frames en el tiempo para identificar regiones con movimiento.
- **Detección de objetos** — modelos de ML analizan las regiones de movimiento para identificar objetos.
- **Grabación y visualización** — configuración determina qué clips y eventos se guardan.

## 14/04/2026
Investigación sobre DeepStream SDK de NVIDIA y su aplicabilidad para el desarrollo de un NVR propio sobre Jetson Orin.

### DeepStream
Framework de NVIDIA construido sobre GStreamer, diseñado específicamente para pipelines de video analytics acelerados por hardware. No es una aplicación standalone sino un toolkit de plugins que se integran en un pipeline GStreamer nativo.

### Compatibilidad
JetPack 6.2 / Ubuntu 22.04 es compatible con DeepStream 7.1, que incluye soporte nativo para CUDA 12.6, TensorRT 10.3, cuDNN 9.3 y DLA 3.1. El stack completo corre sobre el Jetson AGX Orin sin modificaciones.

### What it does
- Adquisición multi-cámara RTSP con reconexión automática.
- Decodificación y scaling completamente en hardware (NVDEC + nvvidconv), liberando CPU y GPU para inferencia.
- Inferencia TensorRT optimizada con batching de múltiples streams.
- Tracking intra-cámara con IDs persistentes.
- Pipeline de grabación hardware (NVENC).
- Output nativo a MQTT — cada detección se publica como JSON con track_id, bbox, confidence, camera_id y timestamp.

### What it doesn't do
- **Motion detection como gatekeeper** — DeepStream no tiene motion detection nativo inteligente. El parámetro `interval` solo saltea frames de forma fija, no condicional. Solución: plugin custom de GStreamer en C++ que corre MOG2 CUDA y hace drop de frames sin movimiento antes de llegar a nvinfer.
- **Re-identificación cross-cámara (MCT)** — nvtracker mantiene IDs solo dentro de una cámara. Una vez la persona sale de frame el ID muere. Para tracking cross-cámara durante el día se requiere una capa adicional con embeddings de apariencia (OSNet x0.25 exportado a TensorRT) y un Re-ID engine que consuma los eventos MQTT de todas las cámaras, compare embeddings contra una base de datos de identidades y asigne Global Person IDs persistentes.
- **Lógica de eventos** — decidir cuándo abrir/cerrar un evento, gap threshold, generación de clips.
- **API REST y dashboard** — gestión de cámaras, consulta de eventos, notificaciones.

### Stack 
| Capa | Tecnología |
|---|---|
| Adquisición + decode | GStreamer + NVDEC (nvv4l2decoder) |
| Motion detection | Plugin GStreamer C++ + MOG2 CUDA |
| Inferencia | YOLOv8 + TensorRT (nvinfer) |
| Tracking intra-cámara | nvtracker (NvDCF) |
| Re-ID embedding | OSNet x0.25 → TensorRT |
| Tracking cross-cámara | Re-ID engine Python + Hungarian matching |
| Mensajería | MQTT (Mosquitto local) |
| Grabación | NVENC (nvv4l2encoder) |
| API | FastAPI (Python) |