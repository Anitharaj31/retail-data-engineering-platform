from kafka import KafkaProducer
import json
import time
import random
import uuid
from datetime import datetime

# Kafka Producer
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x: json.dumps(x).encode("utf-8")
)

# Product Catalog
PRODUCTS = [
    {
        "product_id": "P101",
        "category": "Electronics",
        "price": 799
    },
    {
        "product_id": "P102",
        "category": "Clothing",
        "price": 80
    },
    {
        "product_id": "P103",
        "category": "Home",
        "price": 150
    },
    {
        "product_id": "P104",
        "category": "Sports",
        "price": 120
    }
]

# Payment Methods
PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "PayPal"
]

# Store Locations
LOCATIONS = [
    "New York",
    "Chicago",
    "Dallas",
    "Seattle"
]

print("Starting Kafka Producer...")

TOTAL_MESSAGES = 100

for i in range(TOTAL_MESSAGES):

    product = random.choice(PRODUCTS)
    quantity = random.randint(1, 5)

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": f"C{random.randint(1,500)}",
        "product_id": product["product_id"],
        "product_category": product["category"],
        "quantity": quantity,
        "price": product["price"],
        "total_amount": quantity * product["price"],
        "payment_method": random.choice(PAYMENT_METHODS),
        "store_location": random.choice(LOCATIONS),
        "timestamp": str(datetime.now())
    }

    producer.send("retail_transactions", transaction)

    print(f"Sent {i + 1}/{TOTAL_MESSAGES}")

    # Small delay so Spark can consume smoothly
    time.sleep(0.1)

# Send all buffered messages at once
producer.flush()

producer.close()

print("====================================")
print("Finished sending all messages.")
print("Kafka Producer Completed Successfully.")
print("====================================")