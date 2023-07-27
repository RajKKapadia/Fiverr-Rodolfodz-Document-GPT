import gradio as gr
from fastapi import FastAPI

from document_gpt.helper.gradio_ui import demo
from document_gpt.routers.main import router

app = FastAPI()

app = gr.mount_gradio_app(app, demo, path='/gradio')

app.include_router(router)
