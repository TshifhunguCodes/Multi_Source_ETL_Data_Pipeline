# Multi-Source ETL Data Pipeline

A basic ETL project that generates customer data from multiple source formats, combines the data, cleans it, and loads the cleaned result into a warehouse table.

The project runs locally by default using SQLite. PostgreSQL is optional.

## Project Features

- Generate fake customer data
- Create data in JSON, CSV, TXT, and SQLite formats
- Extract data from all four sources
- Combine source data into one Pandas DataFrame
- Remove duplicates and invalid records
- Save cleaned customer data to CSV
- Load cleaned data into a warehouse database
- Run simple SQL analytics queries
- Optional PostgreSQL loading through `DATABASE_URL`

## Technologies Used

- Python
- Pandas
- Faker
- NumPy
- SQLAlchemy
- SQLite
- PostgreSQL, optional

## Folder Structure

```text
Multi_Source_ETL_Data_Pipeline/
├── analysis/
│   └── analysis_queries.sql
├── analytics/
├── data/
│   ├── clean_customers.csv
│   ├── customers.csv
│   ├── customers.db
│   ├── customers.json
│   └── customers.txt
├── extract/
│   ├── extract_data.py
│   └── generate_data.py
├── ingestion/
├── load/
│   └── load_postgres.py
├── transform/
│   └── clean_data.py
├── warehouse/
│   └── etl_warehouse.db
├── .gitignore
├── README.md
├── requirements.txt
└── run_pipeline.py
```

## What Each Folder Does

| Folder | Purpose |
| --- | --- |
| `analysis/` | Contains SQL queries for reporting and analysis. |
| `analytics/` | Reserved for future analytics files. |
| `data/` | Stores generated source files and cleaned output data. |
| `extract/` | Generates sample data and extracts data from all sources. |
| `ingestion/` | Reserved for future ingestion scripts. |
| `load/` | Loads cleaned data into the warehouse database. |
| `transform/` | Cleans and validates the combined data. |
| `warehouse/` | Stores the local SQLite warehouse database. |

## Pipeline Flow

```text
Generate fake customer data
        ↓
Save source files as JSON, CSV, TXT, and SQLite
        ↓
Extract data from all four sources
        ↓
Combine the extracted data
        ↓
Clean duplicates and invalid values
        ↓
Save cleaned CSV file
        ↓
Load cleaned data into a warehouse table
        ↓
Run SQL analysis queries
```

## Setup Instructions

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Full Pipeline

```bash
python run_pipeline.py
```

Expected output:

```text
Starting ETL Pipeline...
Datasets generated successfully.
Raw records: 84000
Cleaned data saved: data\clean_customers.csv
Cleaned records: 8853
Data loaded into warehouse table: clean_customers
Pipeline completed successfully!
```

The exact cleaned record count can change slightly because the generated data is random.

## Generated Files

After running the pipeline, these files are created:

| File | Description |
| --- | --- |
| `data/customers.json` | Generated customer data in JSON format. |
| `data/customers.csv` | Generated customer data in CSV format. |
| `data/customers.txt` | Generated customer data in pipe-separated TXT format. |
| `data/customers.db` | SQLite source database containing raw customer data. |
| `data/clean_customers.csv` | Cleaned customer dataset. |
| `warehouse/etl_warehouse.db` | Local SQLite warehouse database. |

## Data Cleaning Rules

The transformation step applies these basic rules:

1. Removes duplicate records
2. Removes records with missing `customer_id`
3. Keeps only emails that contain `@`
4. Keeps ages from `18` to `70`
5. Removes negative purchase amounts

## Warehouse Table

The cleaned data is loaded into a table named:

```text
clean_customers
```

By default, the table is stored in:

```text
warehouse/etl_warehouse.db
```

## Analytics Queries

The SQL file is located at:

```text
analysis/analysis_queries.sql
```

It includes queries for:

- Total customers by country
- Average purchase amount
- Total cleaned records
- Top 10 highest spending customers

## Optional PostgreSQL Warehouse

The project uses SQLite by default. To load the cleaned data into PostgreSQL instead, set a `DATABASE_URL` environment variable.

Example:

```bash
DATABASE_URL="postgresql://postgres:password@localhost:5432/data_pipeline" python run_pipeline.py
```

On Windows PowerShell:

```powershell
$env:DATABASE_URL="postgresql://postgres:password@localhost:5432/data_pipeline"
python run_pipeline.py
```

Make sure the PostgreSQL database exists before running the pipeline.

## Main Files

| File | Description |
| --- | --- |
| `run_pipeline.py` | Runs the complete ETL workflow. |
| `extract/generate_data.py` | Generates fake source data in multiple formats. |
| `extract/extract_data.py` | Reads JSON, CSV, TXT, and SQLite source data. |
| `transform/clean_data.py` | Cleans and validates the combined dataset. |
| `load/load_postgres.py` | Loads cleaned data into SQLite by default or PostgreSQL when configured. |
| `analysis/analysis_queries.sql` | Contains simple SQL analytics queries. |

## Notes

- The project is intentionally simple and beginner friendly.
- SQLite is used by default so the project can run without extra database setup.
- PostgreSQL is optional and controlled by `DATABASE_URL`.
- Generated data is fake and should only be used for learning or demos.
