from typing import Protocol
from uuid import UUID

from domain.models.user import User


class UserRepository(Protocol):
    def get_by_id(self, id: UUID) -> User:
        ...

    def get_by_email(self, email: str) -> User:
        ...

    def add(self, user: User):
        ...