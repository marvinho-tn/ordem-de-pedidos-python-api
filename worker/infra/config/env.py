from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    smtp_host: str
    smtp_port: int
    smtp_email_from: str
    orders_api_host: str
    rabbitmq_host: str
    rabbitmq_user: str
    rabbitmq_password: str

    class Config:
        env_file = '.env'

settings = Settings()
