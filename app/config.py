from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str

    messages_collection_name: str = "messages"
    channels_collection_name: str = "channels"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
