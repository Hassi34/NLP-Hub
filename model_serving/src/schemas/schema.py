from pydantic import BaseModel

class InputNER(BaseModel):
    input_str : str
class ShowResultsNER(BaseModel):
    ner_response : str = None

class InputSentiment(BaseModel):
    input_list : list[str]
class ShowResultsSentiment(BaseModel):
    sentiment_analysis_response : str = None

class InputSpeechToText(BaseModel):
    base_64_sound_str : str
class ShowResultsSpeechToText(BaseModel):
    speech_to_text_response : str = None

class InputTextToSpeech(BaseModel):
    input_text : str
class ShowResultsTextToSpeech(BaseModel):
    base_64_sound_str : str = None

class InputTextToGrammerSpellCheck(BaseModel):
    input_text : str
class ShowResultsGrammerSpellCheck(BaseModel):
    response : dict = None

class InputTextSummarization(BaseModel):
    input_text : str
    min_length : int = 30
class ShowResultsTextSummarization(BaseModel):
    summarized_text : str = None