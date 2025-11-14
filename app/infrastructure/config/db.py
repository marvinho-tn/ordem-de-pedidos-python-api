# infrastructure/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infrastructure.config.env import settings
from domain.models.order import Base as orders_base
from domain.models.user import Base as users_base


DATABASE_URL =  settings.database_connection_string

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)

users_base.metadata.create_all(engine)
orders_base.metadata.create_all(engine)

# Dependência para FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
