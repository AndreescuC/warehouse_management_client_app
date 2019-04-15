import pika
import json
import time


PORT = 8003
HOST = "localhost"


def test_connection():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
        connection.close()
    except:
        time.sleep(5)
        test_connection()


class AsyncMessageManager:
    def __init__(self, storage_bridge):
        self.storage_bridge = storage_bridge
        self.populated = False

        test_connection()

        shipment_connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
        self.shipment_channel = shipment_connection.channel()
        self.shipment_channel.queue_declare(queue='shipment', durable=True)

        order_connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
        self.order_channel = order_connection.channel()
        self.order_channel.queue_declare(queue='order', durable=True)

        order_done_connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST, port=PORT))
        self.order_done_channel = order_done_connection.channel()
        self.order_done_channel.queue_declare(queue='order_done', durable=True)

    def receive(self):
        def shipment_callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            self.storage_bridge.set_shipment_info(body)
            self.populated = True

        self.shipment_channel.basic_consume(queue='shipment', on_message_callback=shipment_callback, auto_ack=True)
        print('[x] Waiting for messages.')
        self.shipment_channel.start_consuming()

    def send_shipment_id(self, message):
        self.storage_bridge.set_shipment_id(message)
        message = json.dumps({'content': message})
        headers = {'content_type': 'text/plain', 'type': 'App\Service\Message\RabbitMqMessageOrder'}
        properties = pika.BasicProperties(content_type='text/plain', type='App\Service\Message\RabbitMqMessageOrder', headers=headers)
        self.order_channel.basic_publish(exchange='', routing_key='order', body=message, properties=properties)
        print("[x] Sent shipment id message: ", message)

    def send_order_done(self, message):
        for message in [(order_id, message['source']) for order_id in message['order_id']]:
            if not self.storage_bridge.remove_order_info(message[0]):
                return
            message = json.dumps({'content': message})
            headers = {'content_type': 'text/plain', 'type': 'App\Service\Message\RabbitMqMessageOrderDone'}
            properties = pika.BasicProperties(content_type='text/plain', type='App\Service\Message\RabbitMqMessageOrderDone', headers=headers)
            self.order_done_channel.basic_publish(exchange='', routing_key='order_done', body=message, properties=properties)
            print("[x] Sent order done message: ", message)

    def close(self):
        self.order_channel.close()
        self.shipment_channel.close()
        self.order_done_channel.close()

    def is_already_populated(self):
        return self.populated

    def get_shipment_info(self):
        return self.storage_bridge.orders_info
