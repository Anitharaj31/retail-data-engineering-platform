from kafka import KafkaProducer
import json
import time
import random
import uuid
from datetime import datetime


producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda x:
    json.dumps(x).encode("utf-8")
)


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


PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "PayPal"
]


LOCATIONS = [
    "New York",
    "Chicago",
    "Dallas",
    "Seattle"
]


while True:

    product = random.choice(PRODUCTS)

    quantity = random.randint(1, 5)

    transaction = {

        "transaction_id":
        str(uuid.uuid4()),

        "customer_id":
        "C" + str(random.randint(1, 500)),

        "product_id":
        product["product_id"],

        "product_category":
        product["category"],

        "quantity":
        quantity,

        "price":
        product["price"],

        "total_amount":
        quantity * product["price"],

        "payment_method":
        random.choice(PAYMENT_METHODS),

        "store_location":
        random.choice(LOCATIONS),

        "timestamp":
        str(datetime.now())

    }


    producer.send(
        "retail_transactions",
        transaction
    )


    producer.flush()


    print("Sent:", transaction)


    time.sleep(2)