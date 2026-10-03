from kafka import KafkaConsumer
import json
import os
import logging

logging.basicConfig(level=logging.INFO)
consumer = KafkaConsumer(
    'orders-topic',
    bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='inventory-group'
)

def consume_events():
    logging.info("Consumer actively listening for events...")
    for message in consumer:
        # OpenTelemetry automatically extracts the trace ID to link this step back to the HTTP request
        logging.info(f"Successfully processed event: {message.value}")

if __name__ == "__main__":
    consume_events()