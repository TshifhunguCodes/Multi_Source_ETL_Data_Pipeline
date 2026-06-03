
from extract.generate_data import generate_datasets
from extract.extract_data import extract_all_data
from transform.clean_data import clean_data
from load.load_postgres import load_data

def run_pipeline():
    print("Starting ETL Pipeline...")

    generate_datasets()

    df = extract_all_data()

    print(f"Raw records: {len(df)}")

    cleaned_df = clean_data(df)

    print(f"Cleaned records: {len(cleaned_df)}")

    load_data(cleaned_df)

    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()
