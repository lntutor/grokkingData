import elasticsearch
from kafka import KafkaConsumer
from config import KAFKA_HOST

print KAFKA_HOST

class Base:
    def __init__(self, topic):
        self.topics = [topic]
        self.configs = {
            "bootstrap_servers": KAFKA_HOST
        }

    def consume(self):
        self.connect()
        self.do_consuming()

    def connect(self):
        try:
            self.consumer = KafkaConsumer(*self.topics, **self.configs)
        except elasticsearch.TransportError as e:
            self.handle_transport_error(e)
        except elasticsearch.ConnectionError as e:
            self.handle_connection_error(e)
            self.consumer.close()
            exit(1)

    def handle_transport_error(self, e):
        pass

    def do_consuming(self):
        try:
            for message in self.consumer:
                self.handle(message)
        except elasticsearch.ConnectionError as e:
            self.handle_connection_error(e)
            self.consumer.close()
            exit(1)
        except Exception as e:
            self.handle_connection_error(e)
            self.consumer.close()
            exit(1)
        except KeyboardInterrupt as ki:
            self.consumer.close()

    def handle(self, message):
        pass
