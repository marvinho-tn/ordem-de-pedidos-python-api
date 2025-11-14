from pydantic_settings import BaseSettings

# Classe de configurações da aplicação carregadas de variáveis de ambiente
class Settings(BaseSettings):
    database_connection_string: str
    rabbitmq_host: str
    rabbitmq_user: str
    rabbitmq_password: str

    class Config:
        env_file = '.env'

settings = Settings()
