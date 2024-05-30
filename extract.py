import pandas as pd
from sqlalchemy import create_engine
import logging
import configparser

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

def extract_csv(file_path):
    logger.info(f"Extracting data from {file_path}")
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data extracted successfully from {file_path}")
        return data
    except Exception as e:
        logger.error(f"Error extracting data from {file_path}: {e}")
        raise

def extract_db(connection_string, query):
    logger.info("Extracting data from database")
    try:
        engine = create_engine(connection_string)
        data = pd.read_sql(query, engine)
        logger.info("Data extracted successfully from database")
        return data
    except Exception as e:
        logger.error(f"Error extracting data from database: {e}")
        raise
