from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    DATABASE_NAME: str
    MESSAGES_COLLECTION_NAME: str
    CHANNELS_COLLECTION_NAME: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
