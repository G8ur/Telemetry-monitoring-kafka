from fastapi import FastAPI
from kafka import KafkaProducer
import json
import os

app = FastAPI(title="Order Producer API")
producer = KafkaProducer(
    bootstrap_servers=os.getenv("KAFKA_BROKER", "localhost:9092"),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.post("/orders/")
async def create_order(order_id: int, item: str):
    # OpenTelemetry automatically intercepts this and injects a trace ID into the message headers
    producer.send('orders-topic', {'order_id': order_id, 'item': item})
    producer.flush()
    return {"status": "Event published to broker", "order_id": order_id}