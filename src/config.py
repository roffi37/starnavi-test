from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

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

    model_config = SettingsConfigDict(
        env_file=".env",
    )


database_settings = DatabaseSettings()


class Settings(BaseSettings):
    database: DatabaseSettings = database_settings



def get_settings():
    return Settings(database=database_settings)

