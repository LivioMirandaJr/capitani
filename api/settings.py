from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    db_name: str = "products"
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_host: str = "localhost"
    db_port: int = 5432

    kafka_broker: str = "localhost:9092"
    kafka_topic: str = "produtos-persistidos"


settings = Settings()
