#!/bin/bash

# Run the Python scripts with the YAMLs config files as an argument
python scripts/bigquery_ingest_excel.py config/sample_config_ingest.yaml
python scripts/bigquery_query_trigger.py config/sample_config_query.yaml queries/sample_query.sql
python scripts/bigquery_table_extractor.py config/sample_config_extractor.yaml

# Pause to keep the terminal open after execution
read -p "Press Enter to continue..."