
import pandas as pd
from pathlib import Path

def clean_data(df, output_path="data/clean_customers.csv"):

    df = df.drop_duplicates()

    df = df.dropna(subset=["customer_id"])

    df = df[df["email"].str.contains("@", na=False)]

    df = df[(df["age"] >= 18) & (df["age"] <= 70)]

    df = df[df["purchase_amount"] >= 0]

    output_file = Path(output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)

    print(f"Cleaned data saved: {output_file}")
    return df
