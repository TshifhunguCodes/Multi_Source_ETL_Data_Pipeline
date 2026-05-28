
from extract.extract_data import extract_all_data
from transform.clean_data import clean_data
from load.load_postgres import load_to_postgres

print("Starting ETL Pipeline...")

df = extract_all_data()

print(f"Raw records: {len(df)}")

cleaned_df = clean_data(df)

print(f"Cleaned records: {len(cleaned_df)}")

load_to_postgres(cleaned_df)

print("Pipeline completed successfully!")
