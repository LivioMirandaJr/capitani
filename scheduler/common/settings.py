from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    kafka_broker: str = "localhost:9092"
    kafka_group_id: str = "schedulers"
    kafka_topic: str = "cadastro-produtos"
    kafka_offset: str = "earliest"

    api_endpoint: str = "http://localhost:8000"


settings = Settings()
