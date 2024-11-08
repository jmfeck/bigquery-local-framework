
# BigQuery Local Framework

## Overview

The **BigQuery Local Framework** is a Python-based toolkit for managing data workflows in Google BigQuery - locally. It includes scripts to automate data ingestion, query execution, and data extraction, making it easier to handle common tasks. Each script is customizable via YAML configuration files, providing flexibility for various data workflows.
This is a great tool for data people that don't have total access to all resources of GCP, or people looking for fast prototyping (which was my case).

## Features

- **Ingest Excel Files**: Load data from Excel files into BigQuery.
- **Execute SQL Queries**: Run SQL queries stored in files directly within BigQuery.
- **Extract Table Data**: Export data from a BigQuery table or view to a local file in formats such as CSV, Excel, and Parquet.
- **Extract Query Data**: Export data from a BigQuery query results to a local file in formats such as CSV, Excel, and Parquet.
 
## Project Structure

```plaintext
bigquery-local-framework/
│
├── config/
│   ├── sample_config_query_extractor.yaml      # Configuration for query extraction
│   ├── sample_config_table_extractor.yaml      # Configuration for table extraction
│   ├── sample_config_ingest.yaml               # Configuration for data ingestion
│   └── sample_config_query.yaml                # Configuration for query execution
│
├── input/
│   └── incoming_excel_filename.xlsx            # Sample input file for ingestion
│
├── output/
│   ├── sample_query_export.csv                 # Sample output file for query extraction
│   └── sample_table_export.csv                 # Sample output file for table extraction
│
├── queries/
│   └── sample_query.sql                        # Sample SQL query for BigQuery
│
├── scripts/
│   ├── bigquery_ingest_excel.py                # Script to ingest Excel files into BigQuery
│   ├── bigquery_query_trigger.py               # Script to execute SQL queries in BigQuery
│   ├── bigquery_query_extractor.py             # Script to extract query data from BigQuery
│   └── bigquery_table_extractor.py             # Script to extract table data from BigQuery
│
├── sample_run_pipeline.bash                # Bash script to run the full pipeline
├── sample_run_pipeline.bat                 # Batch script to run the full pipeline on Windows
├── LICENSE
└── README.md
```

## Setup

### Prerequisites

- **Python 3.x**
- **Google Cloud SDK** with BigQuery API enabled
- Required Python packages (install with `requirements.txt`):

```bash
pip install -r requirements.txt
```

### Configuration

Configuration files for each task are located in the `config/` directory. Each YAML file contains settings specific to the task:

- **sample_config_ingest.yaml**: Config for ingesting Excel files.
- **sample_config_query.yaml**: Config for executing queries.
- **sample_config_extractor.yaml**: Config for extracting data.

Customize these files with your project settings.

## Usage

### 1. Ingest Excel Files to BigQuery

To load data from an Excel file into BigQuery:

```bash
python scripts/bigquery_ingest_excel.py config/sample_config_ingest.yaml
```

This script reads an Excel file from the `input/` directory and loads it into the specified BigQuery table.

### 2. Execute SQL Queries in BigQuery

To run a SQL query from the `queries/` directory:

```bash
python scripts/bigquery_query_trigger.py config/sample_config_query.yaml queries/sample_query.sql
```

This will execute the specified SQL query within BigQuery.

### 3. Extract Table Data from BigQuery

The is two ways to extract data from BigQuery.

#### 3.1 Extract Table/View Data

To export table/view from BigQuery to a local file:

```bash
python scripts/bigquery_table_extractor.py config/sample_config_table_extractor.yaml
```

The data will be saved in the `output/` directory in the format specified in the configuration file (CSV, Excel, or Parquet).

#### 3.2 Extract Query Results

To export query results from BigQuery to a local file:

```bash
python scripts/bigquery_query_extractor.py config/sample_config_query_extractor.yaml queries/sample_query.sql
```

The data will be saved in the `output/` directory in the format specified in the configuration file (CSV, Excel, or Parquet).

## Sample Workflow

- **sample_run_pipeline.bash**: Bash script to run the pipeline on Unix-based systems.
- **sample_run_pipeline.bat**: Batch script to run the pipeline on Windows.

These scripts show how to automate ingestion, query execution, and extraction in sequence - a pipeline if you will.

## Example Workflow

1. Place input files in the `input/` directory and set up configuration files in `config/`.
2. Run `bigquery_ingest_excel.py` to load data into BigQuery.
3. Use `bigquery_query_trigger.py` to run SQL transformations or analysis.
4. Run `bigquery_table_extractor.py` to save query results to a local file.

## License

This project is licensed under the MIT License.

---
