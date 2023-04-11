from fastapi import APIRouter, status
import schemas.schema as SCHEMA
from utils.common import read_yaml
from src.prediction_service.services import speech_to_text
from src.utils.common import decode_sound

config = read_yaml('src/configs/config.yaml')

SOUND_SPEECH_TO_TEXT_FILE_PATH = config['model_serving']['SOUND_SPEECH_TO_TEXT_FILE_PATH']

router = APIRouter(
    prefix = '/speech-to-text',
    tags=['Speech to Text']
    )

@router.post('/', response_model=SCHEMA.ShowResultsSpeechToText,
          status_code=status.HTTP_200_OK)
async def speech_2_text(inputParam: SCHEMA.InputSpeechToText):
    base_64_sound_str = inputParam.base_64_sound_str
    decode_sound(sound_str = base_64_sound_str, file_name= SOUND_SPEECH_TO_TEXT_FILE_PATH)
    result = speech_to_text(SOUND_SPEECH_TO_TEXT_FILE_PATH)
    return {"speech_to_text_response": result}