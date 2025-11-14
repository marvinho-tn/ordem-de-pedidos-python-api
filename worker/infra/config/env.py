from pydantic_settings import BaseSettings

# Classe de configurações da aplicação carregadas de variáveis de ambiente
class Settings(BaseSettings):
    smtp_host: str
    smtp_port: int
    orders_api_host: str
    rabbitmq_host: str
    rabbitmq_user: str
    rabbitmq_password: str

    class Config:
        env_file = '.env'

settings = Settings()
