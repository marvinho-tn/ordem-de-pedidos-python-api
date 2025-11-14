from uuid import UUID
from sqlalchemy.orm import Session

from domain.models.user import User
from domain.repositories.user_repository import UserRepository


class PostgresUserRepository(UserRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, id: UUID) -> User:
        return self.session.query(User).filter(User.id == id).first()

    def get_by_email(self, email: str) -> User:
        return self.session.query(User).filter(User.email == email).first()

    def add(self, user: User):
        self.session.add(user)
        self.session.commit()