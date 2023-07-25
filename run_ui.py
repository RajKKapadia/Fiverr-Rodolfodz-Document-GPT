import gradio as gr
from fastapi import FastAPI

from document_gpt.helper.gradio_ui import demo

app = FastAPI()

@app.get('/')
async def home():
    return 'Gradio Web UI is running at the route /gradio.', 200

app = gr.mount_gradio_app(app, demo, path='/gradio')
