import csv
import random
import uuid
from datetime import datetime
from faker import Faker
import os


fake = Faker()


PRODUCTS = [
    {
        "product_id": "P001",
        "category": "Electronics",
        "price": 799.99
    },
    {
        "product_id": "P002",
        "category": "Clothing",
        "price": 49.99
    },
    {
        "product_id": "P003",
        "category": "Home",
        "price": 129.99
    },
    {
        "product_id": "P004",
        "category": "Books",
        "price": 19.99
    },
    {
        "product_id": "P005",
        "category": "Sports",
        "price": 89.99
    }
]


PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "PayPal",
    "Cash"
]


STORES = [
    "New York",
    "Chicago",
    "Dallas",
    "Seattle",
    "Boston"
]


def generate_transaction():

    product = random.choice(PRODUCTS)

    quantity = random.randint(1, 5)

    total_amount = round(
        quantity * product["price"],
        2
    )

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "customer_id": fake.uuid4(),
        "product_id": product["product_id"],
        "product_category": product["category"],
        "quantity": quantity,
        "price": product["price"],
        "total_amount": total_amount,
        "payment_method": random.choice(PAYMENT_METHODS),
        "store_location": random.choice(STORES),
        "timestamp": datetime.now().isoformat()
    }

    return transaction


def generate_csv(file_path, records=1000):

    os.makedirs(
        os.path.dirname(file_path),
        exist_ok=True
    )

    transactions = []

    for _ in range(records):
        transactions.append(
            generate_transaction()
        )


    with open(
        file_path,
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=transactions[0].keys()
        )

        writer.writeheader()

        writer.writerows(transactions)


if __name__ == "__main__":

    output_file = "data/raw/sales.csv"

    generate_csv(
        output_file,
        records=1000
    )

    print("Generated 1000 retail transactions")