from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = "postgresql+psycopg://skilluv:skilluv@localhost:5432/skilluv"
    backend_port: int = 3001
    cors_origin: str = "http://localhost:5173"
    log_level: str = "info"


settings = Settings()
