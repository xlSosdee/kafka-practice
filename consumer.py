from kafka import KafkaConsumer
import json
import os

# Conectar a Kafka usando SSL
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9093")
# Archivos correctos según tu directorio ./certs
SSL_CERT_PATH = "/certs/kafka-cert.pem"  # Certificado del cliente
SSL_KEY_PATH = "/certs/kafka-key-credentials"  # Archivo que podría contener la clave
SSL_CA_PATH = "/certs/kafka.server.truststore.jks"  # Posible autoridad certificadora (CA)

consumer = KafkaConsumer(
    "synthetic_data",
    bootstrap_servers=KAFKA_BROKER,
    security_protocol="SSL",
    ssl_cafile=SSL_CA_PATH,
    ssl_certfile=SSL_CERT_PATH,
    ssl_keyfile=SSL_KEY_PATH,
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id='my-group',  # Añadir el group_id
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

print("📥 Esperando mensajes de Kafka...\n")

for message in consumer:
    print(f"📨 Recibido: {message.value}")
