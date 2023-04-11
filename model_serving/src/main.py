from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run
from utils.common import read_yaml
from routers import (index, ner, sentiment_analysis, speech_to_text,
                      text_to_speech, grammer_spell_check, text_summarization)

config = read_yaml('src/configs/config.yaml')

APP_HOST = config['model_serving']['APP_HOST']
APP_PORT = config['model_serving']['APP_PORT']
API_TITLE = config['model_serving']['API_TITLE']
API_DESCRIPTION = config['model_serving']['API_DESCRIPTION']
API_VERSION = config['model_serving']['API_VERSION']

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
    version=API_VERSION
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(index.router)
app.include_router(ner.router)
app.include_router(sentiment_analysis.router)
app.include_router(speech_to_text.router)
app.include_router(text_to_speech.router)
app.include_router(grammer_spell_check.router)
app.include_router(text_summarization.router)


if __name__ == "__main__":
    app_run(app=app, host=APP_HOST, port=APP_PORT)
