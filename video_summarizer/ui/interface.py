import gradio as gr
import threading
import time
import cv2
from processing.vision_model_clip import analyze_frames
from processing.vision_model_blip2 import generate_summary_blip2
from rtsp.ffmpeg_stream import FFmpegStream

stop_streaming = False
latest_summary = ""

def stream_and_summarize(url, interval, model_name, custom_prompt):
    global stop_streaming, latest_summary
    stop_streaming = False
    interval = int(interval)

    stream = FFmpegStream(url)
    frames = []
    last_summary_time = time.time()

    while not stop_streaming:
        frame = stream.read_frame()
        if frame is None:
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(rgb_frame)

        yield rgb_frame, latest_summary

        if time.time() - last_summary_time >= interval:
            if model_name == "CLIP":
                summary = analyze_frames(frames[-10:], prompts=[custom_prompt] if custom_prompt else None)
            else:
                summary = generate_summary_blip2(frames[-10:])
            latest_summary = summary
            last_summary_time = time.time()

        time.sleep(0.05)

    stream.close()

def stop():
    global stop_streaming
    stop_streaming = True
    return None, "Stream detenido"

def build_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# VSS Local - RTSP Summary con opción de modelo")

        with gr.Row():
            rtsp_input = gr.Textbox(label="RTSP URL", placeholder="rtsp://...")
            interval_input = gr.Number(label="Resumen cada N segundos", value=10)
            model_selector = gr.Radio(choices=["CLIP", "BLIP-2"], label="Modelo de análisis visual", value="CLIP")
        
        prompt_input = gr.Textbox(label="Prompt personalizado (solo CLIP)", placeholder="Ej. una oficina con personas trabajando")

        start_btn = gr.Button("Iniciar")
        stop_btn = gr.Button("Detener")

        video_output = gr.Image(label="Stream en vivo", streaming=True)
        summary_output = gr.Textbox(label="Resumen actual")

        start_btn.click(
            fn=stream_and_summarize,
            inputs=[rtsp_input, interval_input, model_selector, prompt_input],
            outputs=[video_output, summary_output]
        )

        stop_btn.click(
            fn=stop,
            inputs=[],
            outputs=[video_output, summary_output]
        )

    return demo

if __name__ == "__main__":
    demo = build_interface()
    demo.launch()