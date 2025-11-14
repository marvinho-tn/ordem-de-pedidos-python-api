from uuid import UUID
from sqlalchemy.orm import Session

from domain.models.order import Order
from domain.repositories.order_repository import OrderRepository


class PostgresOrderRepository(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order):
        self.session.add(order)
        self.session.commit()

    def get_by_id(self, id: UUID) -> Order:
        return self.session.query(Order).filter(Order.id == id).first()

    def update_order(self, order: Order):
        self.session.merge(order)
        self.session.commit()
