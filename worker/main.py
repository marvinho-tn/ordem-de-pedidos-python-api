import pika

from consumers.orders_consumer import handle_order
from infra.config.env import settings


def main():
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
    result = channel.queue_declare(queue="orders_queue", exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key="orders.new")

    print("[*] Worker listening for orders...")

    channel.basic_consume(queue=queue_name, on_message_callback=handle_order, auto_ack=True)
    channel.start_consuming()

if __name__ == "__main__":
    main()
