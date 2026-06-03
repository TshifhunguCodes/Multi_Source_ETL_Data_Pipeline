
from faker import Faker
import pandas as pd
import random
import sqlite3
from pathlib import Path

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

def generate_datasets(size=20000, output_dir="data"):
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    df = create_dataset(size)

    df.to_json(output_path / "customers.json", orient="records")
    df.to_csv(output_path / "customers.csv", index=False)
    df.to_csv(output_path / "customers.txt", sep="|", index=False)

    conn = sqlite3.connect(output_path / "customers.db")
    df.to_sql("customers", conn, if_exists="replace", index=False)
    conn.close()

    print("Datasets generated successfully.")
    return df


if __name__ == "__main__":
    generate_datasets()
