from fastapi import APIRouter, status
import schemas.schema as SCHEMA
from utils.common import read_yaml
from src.prediction_service.services import speech_to_text, text_to_speech
from src.utils.common import decode_sound

config = read_yaml('src/configs/config.yaml')

SOUND_TEXT_TO_SPEECH_FILE_PATH = config['model_serving']['SOUND_TEXT_TO_SPEECH_FILE_PATH']

router = APIRouter(
    prefix = '/text-to-speech',
    tags=['Text to Speech']
    )

@router.post('/', response_model=SCHEMA.ShowResultsTextToSpeech,
          status_code=status.HTTP_200_OK)
async def text_2_speech(inputParam: SCHEMA.InputTextToSpeech):
    input_text = inputParam.input_text
    base_64_sound_str = text_to_speech(input_text, SOUND_TEXT_TO_SPEECH_FILE_PATH)
    return {"base_64_sound_str": base_64_sound_str}