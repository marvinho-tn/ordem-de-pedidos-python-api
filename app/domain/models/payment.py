import datetime
from uuid import UUID

from value_objects.payment_method import PaymentMethod
from value_objects.payment_status import PaymentStatus


class Payment:
    id: UUID
    order_id: UUID
    status: PaymentStatus
    amount: float
    payment_method: PaymentMethod
    transaction_id: UUID
    created_at: datetime