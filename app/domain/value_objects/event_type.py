from enum import Enum


class EventType(Enum):
    ORDER_PLACED = 'order_placed'
    PAYMENT_CONFIRMED = 'payment_confirmed'