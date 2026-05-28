
import pandas as pd
import sqlite3

def extract_all_data():

    json_df = pd.read_json("data/customers.json")

    csv_df = pd.read_csv("data/customers.csv")

    txt_df = pd.read_csv("data/customers.txt", sep="|")

    conn = sqlite3.connect("data/customers.db")
    db_df = pd.read_sql("SELECT * FROM customers", conn)
    conn.close()

    combined_df = pd.concat([
        json_df,
        csv_df,
        txt_df,
        db_df
    ])

    return combined_df
