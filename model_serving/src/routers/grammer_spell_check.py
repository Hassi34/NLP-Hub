from fastapi import APIRouter, status
import schemas.schema as SCHEMA
from gingerit.gingerit import GingerIt


router = APIRouter(
    prefix = '/grammer-spell-check',
    tags=['Grammer and Spell Check']
    )

@router.post('/', response_model=SCHEMA.ShowResultsGrammerSpellCheck,
          status_code=status.HTTP_200_OK)
async def grammer_and_spell_check(inputParam: SCHEMA.InputTextToGrammerSpellCheck):
    input_text = inputParam.input_text
    parser = GingerIt()
    result = parser.parse(input_text)
    return {"response": result}