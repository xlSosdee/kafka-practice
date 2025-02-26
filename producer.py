from kafka import KafkaProducer
import json
import uuid
import random
import time
from datetime import datetime

# Configurar el productor de Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("📤 Enviando mensajes a Kafka en el tópico 'synthetic_data'...\n")

while True:
    mensaje = {
        "id": str(uuid.uuid4()),
        "nombre": random.choice(["Alice", "Bob", "Charlie", "David"]),
        "email": f"test{random.randint(1, 100)}@example.com",
        "pais": random.choice(["Peru", "Mexico", "Argentina", "Colombia"]),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("synthetic_data", mensaje)
    print(f"✅ Enviado: {mensaje}")
    time.sleep(2)  # Espera 2 segundos antes de enviar otro mensaje
