from kafka import KafkaConsumer
import json
import os

# Conectar a Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

consumer = KafkaConsumer(
    "synthetic_data",
    bootstrap_servers=KAFKA_BROKER,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("📥 Esperando mensajes de Kafka...\n")

for message in consumer:
    print(f"📨 Recibido: {message.value}")
