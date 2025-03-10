from kafka import KafkaProducer
import json
import uuid
import random
import time
from datetime import datetime
import os

# Conectar a Kafka usando SSL
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9093")
# Archivos correctos según tu directorio ./certs
SSL_CERT_PATH = "/certs/kafka-cert.pem"  # Certificado del cliente
SSL_KEY_PATH = "/certs/kafka-key-credentials"  # Archivo que podría contener la clave
SSL_CA_PATH = "/certs/kafka.server.truststore.jks"  # Posible autoridad certificadora (CA)

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    security_protocol="SSL",
    ssl_cafile=SSL_CA_PATH,
    ssl_certfile=SSL_CERT_PATH,
    ssl_keyfile=SSL_KEY_PATH,
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
    time.sleep(2)
