from functools import lru_cache

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Base(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

class DatabaseSettings(Base):
    POSTGRES_HOST: str = Field(default="localhost")
    POSTGRES_PORT: str = Field(default="5432")
    POSTGRES_USER: str = Field(default="user")
    POSTGRES_PASSWORD: str = Field(default="password")
    POSTGRES_DB: str = Field(default="db")

    def generate_async_database_url(self) -> str:
        url = (
            "postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:"
            f"{self.POSTGRES_PORT}/"
            f"{self.POSTGRES_DB}"
        )
        return url

class OpenAISettings(Base):
    API_KEY: str = Field(default="token")


class JWTSettings(Base):
    JWT_SECRET_KEY: str = Field(default="token")
    ALGORITHM: str = Field(default="HS256")


class Settings(BaseModel):

    database: DatabaseSettings = DatabaseSettings()
    openai: OpenAISettings = OpenAISettings()
    jwt_settings: JWTSettings = JWTSettings()


@lru_cache
def get_settings():
    return Settings()
