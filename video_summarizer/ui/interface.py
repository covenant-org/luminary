import gradio as gr
import time
import cv2
import logging
from datetime import datetime
from processing.vision_model_clip import analyze_frames
from processing.vision_model_blip2 import generate_summary_blip2
from processing.vision_model_llava import generate_summary_llava
from rtsp.ffmpeg_stream import FFmpegStream

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

stop_streaming = False
latest_summary = ""
current_model = "CLIP"
analysis_history = []

def stream_and_summarize(url, interval, model_name, custom_prompt, llava_model_size, 
                         max_tokens, temperature, top_p, num_beams, repetition_penalty, length_penalty):
    global stop_streaming, latest_summary, current_model, analysis_history
    stop_streaming = False
    current_model = model_name
    interval = int(interval)
    analysis_history = []

    try:
        stream = FFmpegStream(url)
    except Exception as e:
        logger.error(f"Error al iniciar stream: {str(e)}")
        latest_summary = f"Error al conectar con RTSP: {str(e)}"
        yield None, latest_summary, ""
        return

    frames = []
    last_summary_time = time.time()
    consecutive_none_frames = 0

    while not stop_streaming:
        try:
            frame = stream.read_frame()
            
            if frame is None:
                consecutive_none_frames += 1
                if consecutive_none_frames > 10:
                    logger.error("Demasiados frames nulos consecutivos, deteniendo stream")
                    break
                time.sleep(0.1)
                continue
            
            consecutive_none_frames = 0
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(rgb_frame)
            
            if len(frames) > 100:
                frames = frames[-100:]

            history_text = format_history()
            yield rgb_frame, latest_summary, history_text

            if time.time() - last_summary_time >= interval and len(frames) >= 5:
                try:
                    valid_frames = [f for f in frames[-10:] if f is not None]
                    
                    if not valid_frames:
                        logger.warning("No hay frames válidos para análisis")
                        continue
                        
                    if model_name == "CLIP":
                        summary = analyze_frames(valid_frames, prompts=[custom_prompt] if custom_prompt else None)
                    elif model_name == "BLIP-2":
                        summary = generate_summary_blip2(valid_frames)
                    elif model_name == "LLaVA":
                        generation_params = {
                            'max_tokens': max_tokens,
                            'temperature': temperature,
                            'top_p': top_p,
                            'num_beams': num_beams,
                            'repetition_penalty': repetition_penalty,
                            'length_penalty': length_penalty
                        }
                        summary = generate_summary_llava(
                            valid_frames, 
                            custom_prompt, 
                            llava_model_size,
                            generation_params
                        )
                    
                    latest_summary = summary
                    last_summary_time = time.time()
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    analysis_history.append(f"[{timestamp}] {model_name}:\n{summary}\n")
                    
                    history_text = format_history()
                    
                except Exception as e:
                    logger.error(f"Error en generación de resumen: {str(e)}", exc_info=True)
                    latest_summary = f"Error en modelo {model_name}: {str(e)}"
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    analysis_history.append(f"[{timestamp}] ERROR:\n{latest_summary}\n")
                    history_text = format_history()

            time.sleep(0.02)
            
        except Exception as e:
            logger.error(f"Error durante el streaming: {str(e)}", exc_info=True)
            latest_summary = f"Error en el stream: {str(e)}"
            break

    stream.close()
    logger.info("Stream cerrado")
    yield None, latest_summary, format_history()

def format_history():
    if not analysis_history:
        return "Historial de análisis:\n----------------------\n\n"
    
    history_text = "Historial de análisis (más reciente primero):\n-----------------------------------------------\n\n"
    for entry in reversed(analysis_history[-10:]):
        history_text += f"{entry}\n{'-'*80}\n"
    return history_text

def stop():
    global stop_streaming
    stop_streaming = True
    return None, "Stream detenido", format_history()

def build_interface():
    css = """
    .scrollable {max-height: 500px; overflow-y: auto !important;}
    .panel {border: 1px solid #e0e0e0; border-radius: 8px; padding: 15px; margin-bottom: 15px;}
    .summary-box {min-height: 200px;}
    .history-box {min-height: 400px;}
    .params-grid {display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;}
    .llava-params {border: 1px solid #4CAF50; padding: 15px; border-radius: 8px; margin-top: 10px;}
    """
    
    with gr.Blocks(theme=gr.themes.Soft(), css=css) as demo:
        gr.Markdown("# VSS Local - Análisis de Video en Tiempo Real")
        
        with gr.Row():
            # Columna izquierda: Controles
            with gr.Column(scale=1):
                gr.Markdown("## Configuración")
                with gr.Group(elem_classes="panel"):
                    rtsp_input = gr.Textbox(
                        label="URL RTSP", 
                        placeholder="rtsp://...",
                        value="rtsp://admin:L2F4FD58@192.168.10.90:554/cam/realmonitor?channel=1&subtype=0"
                    )
                    
                    with gr.Row():
                        interval_input = gr.Slider(
                            label="Resumen cada (segundos)", 
                            value=20,
                            minimum=5,
                            maximum=120,
                            step=5
                        )
                        model_selector = gr.Dropdown(
                            choices=["CLIP", "BLIP-2", "LLaVA"],
                            label="Modelo de análisis", 
                            value="LLaVA"
                        )
                    
                    # Grupo para controles de LLaVA - SOLUCIÓN SIMPLIFICADA
                    llava_group = gr.Group(visible=True, elem_classes="llava-params")
                    with llava_group:
                        with gr.Row():
                            llava_size_selector = gr.Radio(
                                choices=["7b", "13b"],
                                label="Tamaño de modelo",
                                value="7b"
                            )
                        
                        gr.Markdown("### Parámetros de Generación")
                        with gr.Row():
                            with gr.Column():
                                max_tokens = gr.Slider(
                                    label="Máximo de tokens",
                                    minimum=50,
                                    maximum=1000,
                                    step=50,
                                    value=300
                                )
                                temperature = gr.Slider(
                                    label="Temperatura",
                                    minimum=0.1,
                                    maximum=1.0,
                                    step=0.05,
                                    value=0.6
                                )
                                top_p = gr.Slider(
                                    label="Top-P",
                                    minimum=0.5,
                                    maximum=1.0,
                                    step=0.05,
                                    value=0.95
                                )
                            with gr.Column():
                                num_beams = gr.Slider(
                                    label="Número de vigas",
                                    minimum=1,
                                    maximum=5,
                                    step=1,
                                    value=2
                                )
                                repetition_penalty = gr.Slider(
                                    label="Penalización de repetición",
                                    minimum=1.0,
                                    maximum=2.0,
                                    step=0.1,
                                    value=1.2
                                )
                                length_penalty = gr.Slider(
                                    label="Penalización de longitud",
                                    minimum=0.5,
                                    maximum=2.0,
                                    step=0.1,
                                    value=1.3
                                )
                    
                    prompt_input = gr.Textbox(
                        label="Prompt personalizado", 
                        placeholder="Ej: Describe las personas y objetos...",
                        lines=3,
                        value="Describe escena, objetos principales y acciones visibles. Responde en español."
                    )
                    
                    with gr.Row():
                        start_btn = gr.Button("Iniciar Análisis", variant="primary")
                        stop_btn = gr.Button("Detener", variant="stop")
            
            # Columna derecha: Visualización
            with gr.Column(scale=2):
                # Video
                with gr.Group(elem_classes="panel"):
                    video_output = gr.Image(
                        label="Video en Vivo", 
                        streaming=True,
                        width=640
                    )
                
                # Resúmenes
                with gr.Tabs():
                    with gr.Tab("Resumen Actual"):
                        summary_output = gr.Textbox(
                            label="Análisis más reciente",
                            interactive=False,
                            lines=8,
                            max_lines=20,
                            elem_classes=["summary-box"],
                            show_copy_button=True
                        )
                    
                    with gr.Tab("Historial Completo"):
                        history_output = gr.Textbox(
                            label="Historial de Análisis",
                            interactive=False,
                            lines=20,
                            max_lines=100,
                            elem_classes=["history-box", "scrollable"],
                            show_copy_button=True
                        )

        # SOLUCIÓN ALTERNATIVA: Eliminamos la función de toggle y mostramos siempre los controles
        # Los controles solo se usarán cuando se seleccione LLaVA de todos modos

        start_btn.click(
            fn=stream_and_summarize,
            inputs=[
                rtsp_input, 
                interval_input, 
                model_selector, 
                prompt_input, 
                llava_size_selector,
                max_tokens,
                temperature,
                top_p,
                num_beams,
                repetition_penalty,
                length_penalty
            ],
            outputs=[video_output, summary_output, history_output]
        )

        stop_btn.click(
            fn=stop,
            inputs=[],
            outputs=[video_output, summary_output, history_output]
        )

    return demo

if __name__ == "__main__":
    logger.info("Iniciando aplicación Gradio")
    demo = build_interface()
    demo.launch(server_port=7860, share=False)