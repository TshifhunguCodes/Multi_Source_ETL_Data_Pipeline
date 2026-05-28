
from sqlalchemy import create_engine

def load_to_postgres(df):

    username = "postgres"
    password = "password"
    host = "localhost"
    port = "5432"
    database = "data_pipeline"

    engine = create_engine(
        f"postgresql://{username}:{password}@{host}:{port}/{database}"
    )

    df.to_sql(
        "clean_customers",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded into PostgreSQL.")
