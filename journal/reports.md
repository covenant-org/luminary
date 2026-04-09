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