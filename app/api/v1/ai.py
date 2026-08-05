from fastapi import APIRouter
from fastapi import Depends

from app.schemas.request import GenerateRequest
from app.schemas.response import GenerateResponse

from app.services.ai_service import generate_text

from app.core.security import verify_api_key

from app.core.auth import get_current_user



router = APIRouter(
    prefix="/api/v1",
    tags=["AI"]
)


@router.post(
    "/generate",
    response_model=GenerateResponse
)

async def generate(
    request: GenerateRequest,
    current_user = Depends(
        get_current_user
    )
):

    result = await generate_text(
        request.prompt
    )

    return GenerateResponse(
        response=result,
        status="success"
    )