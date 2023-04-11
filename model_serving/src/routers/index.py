from fastapi import APIRouter
from starlette.responses import RedirectResponse


router = APIRouter(
    tags=['Authentication']
    )

@router.get("/")
async def index():
    return RedirectResponse(url="/docs")
