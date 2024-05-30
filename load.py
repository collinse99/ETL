def load_csv(data, destination_file):
    logger.info(f"Loading data into {destination_file}")
    try:
        data.to_csv(destination_file, index=False)
        logger.info(f"Data loaded successfully into {destination_file}")
    except Exception as e:
        logger.error(f"Error loading data into {destination_file}: {e}")
        raise

def load_db(data, connection_string, table_name):
    logger.info("Loading data into database")
    try:
        engine = create_engine(connection_string)
        data.to_sql(table_name, engine, if_exists='replace', index=False)
        logger.info("Data loaded successfully into database")
    except Exception as e:
        logger.error(f"Error loading data into database: {e}")
        raise
