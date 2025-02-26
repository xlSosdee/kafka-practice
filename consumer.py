from kafka import KafkaConsumer
import json

# Configurar el consumidor de Kafka
consumer = KafkaConsumer(
    "synthetic_data",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("📥 Esperando mensajes de Kafka...\n")

# Leer mensajes en un bucle
for message in consumer:
    print(f"📨 Recibido: {message.value}")
