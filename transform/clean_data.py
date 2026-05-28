
import pandas as pd

def clean_data(df):

    df = df.drop_duplicates()

    df = df.dropna(subset=["customer_id"])

    df = df[df["email"].str.contains("@", na=False)]

    df = df[(df["age"] >= 18) & (df["age"] <= 70)]

    df = df[df["purchase_amount"] >= 0]

    return df
