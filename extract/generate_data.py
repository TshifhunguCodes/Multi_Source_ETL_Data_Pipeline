
from faker import Faker
import pandas as pd
import random
import sqlite3

fake = Faker()

def create_dataset(size=20000):
    data = []

    for i in range(size):
        row = {
            "customer_id": i,
            "name": fake.name(),
            "email": fake.email() if random.random() > 0.1 else "invalid_email",
            "age": random.randint(-5, 100),
            "country": fake.country(),
            "purchase_amount": round(random.uniform(-100, 5000), 2)
        }

        data.append(row)

    df = pd.DataFrame(data)

    duplicates = df.sample(1000)
    df = pd.concat([df, duplicates])

    return df

df = create_dataset()

df.to_json("../data/customers.json", orient="records")
df.to_csv("../data/customers.csv", index=False)

df.to_csv("../data/customers.txt", sep="|", index=False)

conn = sqlite3.connect("../data/customers.db")
df.to_sql("customers", conn, if_exists="replace", index=False)
conn.close()

print("Datasets generated successfully.")
