def transform(data):
    logger.info("Transforming data")
    try:
        # Example transformation: filter rows where 'age' is greater than 18
        filtered_data = data[data['age'] > 18]

        # Example transformation: create a new column 'age_in_months'
        filtered_data['age_in_months'] = filtered_data['age'] * 12

        # More transformations can be added here
        logger.info("Data transformed successfully")
        return filtered_data
    except Exception as e:
        logger.error(f"Error transforming data: {e}")
        raise
