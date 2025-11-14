import json
import pika

from domain.models.order import Order
from domain.models.user import User
from infrastructure.config.env import settings


def publish_order(order: Order, user: User):
    credentials = pika.PlainCredentials(
        username=settings.rabbitmq_user,
        password=settings.rabbitmq_password
    )

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=settings.rabbitmq_host,
            port=5672,
            credentials=credentials
        )
    )
    channel = connection.channel()
    exchange_name = "orders"

    channel.exchange_declare(exchange=exchange_name, exchange_type="topic")

    message = {
        "id": str(order.id),
        "user_id": str(order.user_id),
        "email": user.email
    }

    channel.basic_publish(
        exchange=exchange_name,
        routing_key="orders.new",
        body=json.dumps(message)
    )

    print(f'Order created message successed published: {message}')

    connection.close()
