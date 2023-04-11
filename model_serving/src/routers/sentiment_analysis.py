from fastapi import APIRouter, status
import schemas.schema as SCHEMA
from src.prediction_service.services import analyze_sentiment


router = APIRouter(
    prefix = '/sentiment-analysis',
    tags=['Sentiment Analysis']
    )

@router.post('/', response_model=SCHEMA.ShowResultsSentiment,
          status_code=status.HTTP_200_OK)
async def sentiment_analysis(inputParam: SCHEMA.InputSentiment):
    input_list = inputParam.input_list
    result = analyze_sentiment(input_list)
    return {"sentiment_analysis_response": result}