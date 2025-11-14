import datetime
from uuid import UUID


class Product:
    id: UUID
    name: str
    description: str
    price: float
    stock_quantity: int
    created_at: datetime