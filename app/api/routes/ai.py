from fastapi import APIRouter

from app.schemas.request import GenerateRequest
from app.schemas.response import GenerateResponse

from app.services.ai_service import generate_text


router = APIRouter(
    prefix="/api/v1",
    tags=["AI"]
)


@router.post(
    "/generate",
    response_model=GenerateResponse
)
def generate(
    request: GenerateRequest
):

    result = generate_text(
        request.prompt
    )


    return GenerateResponse(
        response=result,
        status="success"
    )