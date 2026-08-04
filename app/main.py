from fastapi import FastAPI

from app.api.routes import health
from app.api.routes import ai

app = FastAPI(
    title="Production API Wrapper",
    version="1.0.0"
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