from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Production API Wrapper"

    VERSION: str = "1.0.0"

    DEBUG: bool = True

    GEMINI_API_KEY: str = ""

    DATABASE_URL: str = ""

    JWT_SECRET: str = ""

    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    REDIS_URL: str = ""

    class Config:

        env_file = ".env"


settings = Settings()