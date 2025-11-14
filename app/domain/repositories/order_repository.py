from typing import Protocol
from uuid import UUID

from domain.models.order import Order


class OrderRepository(Protocol):
    def add(self, order: Order):
        ...

    def get_by_id(self, id: UUID) -> Order:
        ...

    def update(self, order: Order):
        ...