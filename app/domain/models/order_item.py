import datetime
from uuid import UUID


class OrderItem:
    id: UUID
    order_id: UUID
    product_id: UUID
    quantity: int
    unit_price: float
    created_at: datetime