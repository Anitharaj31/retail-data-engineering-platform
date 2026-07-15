import random
import json
import time
from datetime import datetime


products = [
    {
        "product_id": "P101",
        "category": "Electronics",
        "price": 500
    },
    {
        "product_id": "P102",
        "category": "Clothing",
        "price": 80
    },
    {
        "product_id": "P103",
        "category": "Food",
        "price": 20
    },
    {
        "product_id": "P104",
        "category": "Furniture",
        "price": 300
    }
]


while True:

    product = random.choice(products)

    transaction = {

        "transaction_id": random.randint(10000,99999),

        "customer_id": "C" + str(random.randint(1,500)),

        "product_id": product["product_id"],

        "category": product["category"],

        "quantity": random.randint(1,5),

        "price": product["price"],

        "timestamp": str(datetime.now())
    }


    with open("../../data/live_transactions.json","a") as file:
        file.write(json.dumps(transaction) + "\n")


    print(transaction)

    time.sleep(2)
