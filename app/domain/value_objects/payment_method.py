from enum import Enum


class PaymentMethod(Enum):
    CREDIT_CARD = 'credit_card'
    PIX = 'pix'
    BOLETO = 'boleto'