
from fastapi import HTTPException, status

from transformers import AutoModelForTokenClassification
from transformers import BertTokenizerFast
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import speech_recognition as sr
from gtts import gTTS
from src.utils.common import encode_sound

def predict_ner(input_str : str, ner_model_path: str) -> list:
    model_fine_tuned = AutoModelForTokenClassification.from_pretrained(ner_model_path)
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")
    ner = pipeline("ner", model=model_fine_tuned, tokenizer=tokenizer)
    ner_results = ner(input_str)

    if isinstance(ner_results, list):
        return str(ner_results)
    else:
        message = "Unexpected prediction values"
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                            detail=message)
    
def analyze_sentiment(input_list : list) -> list[dict]:
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"

    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    classifier = pipeline('sentiment-analysis', model = model, tokenizer= tokenizer)
    res = classifier(input_list)

    if isinstance(res, list):
        return str(res)
    else:
        message = "Unexpected prediction values"
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                            detail=message)

def speech_to_text(audio_file_path : str) -> str :
    r = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio = r.record(source)
    try:
        textdata = r.recognize_google(audio)
        if isinstance(textdata, str):
            return textdata
        else:
            message = "Unexpected prediction values"
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                                detail=message)
    
    except sr.UnknownValueError:
        message = "Audio Error"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=message)


def text_to_speech(input_text: str, output_audio_file_path: str) -> str:
    tts = gTTS(text=input_text, lang='en', slow=False)
    tts.save(output_audio_file_path)  # save file as ... (here saving as mp3)
    base64_sound = encode_sound(output_audio_file_path)
    
    if isinstance(base64_sound, str):
        return base64_sound
    else:
        message = "Unexpected prediction values"
        raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED,
                            detail=message)
