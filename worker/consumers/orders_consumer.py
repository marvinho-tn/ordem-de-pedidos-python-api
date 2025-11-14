import json
import logging

from infra.config.env import settings
from infra.config.email import send_email
from services.order_external_service import OrderExternalService

logger = logging.getLogger("orders_consumer")

def handle_order(ch, method, properties, body):
    logger.info(f'Start processing order message...')

    message = json.loads(body)
    email = message["email"]
    order_id = message["id"]

    status = OrderExternalService.update_status(order_id)

    if status is None:
        return

    link = f'{settings.orders_api_host}/orders/{order_id}/update-status'

    mail_message = f'Clique no link para aprovar o pedido: {link}'

    send_email(email, 'Seu pedido precisa de aprovação', mail_message)

    logger.info('Email message sended, process finished worker.')