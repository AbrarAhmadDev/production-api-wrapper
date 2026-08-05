from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.v1 import health
from app.api.v1 import ai
from app.api.v1 import auth

from app.core.exceptions import APIException
from app.middleware.logging import LoggingMiddleware

app = FastAPI(
    title="Production API Wrapper",
    version="1.0.0"
)

app.include_router(
    auth.router
)

app.add_middleware(
    LoggingMiddleware
)

app.include_router(
    health.router
)

app.include_router(
    ai.router
)

@app.get("/")
def root():

    return {
        "message":"API running"
    }

@app.exception_handler(APIException)
async def api_exception_handler(
    request,
    exc: APIException
):

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.message,
            "data": exc.data
        }
    )