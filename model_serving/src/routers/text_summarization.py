from fastapi import APIRouter, status
import schemas.schema as SCHEMA
from transformers import pipeline

router = APIRouter(
    prefix = '/text-summarization',
    tags=['Text Summarization']
    )

@router.post('/', response_model=SCHEMA.ShowResultsTextSummarization,
          status_code=status.HTTP_200_OK)
async def sentiment_analysis(inputParam: SCHEMA.InputTextSummarization):
    input_text = inputParam.input_text
    min_length = inputParam.min_length
    summarizer = pipeline('summarization', min_length = min_length, model = 'google/pegasus-xsum')
    result = summarizer(input_text)
    return {"summarized_text": str(result)}