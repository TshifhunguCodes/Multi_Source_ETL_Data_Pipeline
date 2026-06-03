
from sqlalchemy import create_engine
import os

def load_data(df, table_name="clean_customers"):
    database_url = os.getenv("DATABASE_URL", "sqlite:///warehouse/etl_warehouse.db")

    engine = create_engine(database_url)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"Data loaded into warehouse table: {table_name}")


def load_to_postgres(df):
    load_data(df)
