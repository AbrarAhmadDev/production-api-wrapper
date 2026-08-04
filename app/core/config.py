from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "Production API Wrapper"

    version: str = "1.0.0"

    debug: bool = True


    class Config:
        env_file = ".env"


settings = Settings()