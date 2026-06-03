
import pandas as pd
import sqlite3
from pathlib import Path

def extract_all_data(data_dir="data"):
    data_path = Path(data_dir)

    json_df = pd.read_json(data_path / "customers.json")

    csv_df = pd.read_csv(data_path / "customers.csv")

    txt_df = pd.read_csv(data_path / "customers.txt", sep="|")

    conn = sqlite3.connect(data_path / "customers.db")
    db_df = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()

    combined_df = pd.concat([
        json_df,
        csv_df,
        txt_df,
        db_df
    ])

    return combined_df
