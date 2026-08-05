from fastapi import FastAPI

from app.api.v1 import health
from app.api.v1 import ai

from app.core.exceptions import APIException
from app.middleware.logging import LoggingMiddleware

app = FastAPI(
    title="Production API Wrapper",
    version="1.0.0"
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