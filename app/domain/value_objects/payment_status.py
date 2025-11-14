from enum import Enum


class PaymentStatus(Enum):
    INITIATED = 'initiated'
    CONFIRMED = 'confirmed'
    FAILED = 'failed'