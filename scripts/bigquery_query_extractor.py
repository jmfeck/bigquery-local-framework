# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import yaml
import sys
import pandas as pd
import pandas_gbq as pdbq
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

###############################################################################################################
# Config file reader
###############################################################################################################
def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    logging.info(f"Configuration loaded from {file_path}")
    return config

conn_config_file_path = sys.argv[1]
query_file_path = sys.argv[2]

config = load_config(conn_config_file_path)

###############################################################################################################
# Functions
###############################################################################################################
def get_config_item(config_section, var):
    """Retrieve a configuration item and ensure it's not empty."""
    try:
        val = config_section[var]
        if not val:
            raise ValueError(f"{var} cannot be an empty string")
        logging.info(f"{var}: {val}")
        return val
    except KeyError as e:
        logging.error(f"Missing configuration for {var}")
        sys.exit(1)

def load_query(query_file_path):
    """Load query from a SQL file."""
    with open(query_file_path, 'r') as file:
        query = file.read()
    logging.info(f"Query loaded from {query_file_path}")
    return query

###############################################################################################################
# Get config values
###############################################################################################################
output_foldername = get_config_item(config['project_param'], 'output_foldername')
file_radc = get_config_item(config['file_param'], 'file_radcname')
file_ext = get_config_item(config['file_param'], 'file_ext')
file_sheetname = get_config_item(config['file_param'], 'sheet_name')

###############################################################################################################
# Path Handling
###############################################################################################################
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_output = os.path.join(path_project, output_foldername)
os.makedirs(path_output, exist_ok=True)
path_file = os.path.join(path_output, f"{file_radc}{file_ext}")

###############################################################################################################
# Main Process
###############################################################################################################
logging.info("Reading query from file")
query = load_query(query_file_path)

logging.info("Executing query in BigQuery")
df = pdbq.read_gbq(query)

logging.info("Exporting results")
exporters = {
    ".parquet": lambda df, path: df.to_parquet(path, index=False),
    ".csv": lambda df, path: df.to_csv(path, index=False),
    ".xlsx": lambda df, path: df.to_excel(path, sheet_name=file_sheetname, index=False)
}
try:
    exporters[file_ext](df, path_file)
    logging.info(f"Results exported successfully to {path_file}")
except KeyError:
    logging.error(f"Unsupported file extension: {file_ext}")