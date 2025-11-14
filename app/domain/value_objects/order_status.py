from shared.base_enum import BaseEnum


class OrderStatus(BaseEnum):
    PENDING = 'pending'
    PAID = 'paid'
    CANCELLED = 'cancelled'
    WAITING_PAYMENT = 'waiting_payment'