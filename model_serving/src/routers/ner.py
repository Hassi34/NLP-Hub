from fastapi import APIRouter, status
from utils.common import read_yaml
import schemas.schema as SCHEMA
from src.prediction_service.services import predict_ner

config = read_yaml('src/configs/config.yaml')

NER_PRODUCTION_MODEL_PATH = config['model_serving']['NER_PRODUCTION_MODEL_PATH']

router = APIRouter(
    prefix = '/named-entity-recognition',
    tags=['Named Entity Recognition (NER)']
    )

@router.post('/', response_model=SCHEMA.ShowResultsNER,
          status_code=status.HTTP_200_OK)
async def named_entity_recognition(inputParam: SCHEMA.InputNER):
    input_str = inputParam.input_str
    ner_result = predict_ner(input_str, NER_PRODUCTION_MODEL_PATH)
    return {"ner_response": ner_result}