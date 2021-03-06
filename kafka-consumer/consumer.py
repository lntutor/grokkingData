TOPIC = 'vidsell'

import json

from connection import consumer, elastic


class LogsConsumer(consumer.Base):
    def handle(self, message):
        json_log = json.loads(message.value)
        metric = json_log.get('metric', None)
        print metric
        if not metric:
            return
        result = elastic.client.index(index="vidsell", doc_type=metric, body=json_log)
        print str(result)

    def handle_connection_error(self, e):
        print str(e)


if __name__ == "__main__":
    c = LogsConsumer(TOPIC)
    c.consume()
