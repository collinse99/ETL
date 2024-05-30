if __name__ == "__main__":
    # Extract
    csv_data = extract_csv(config['SOURCE']['CsvFilePath'])
    db_data = extract_db(config['SOURCE']['DbConnectionString'], config['SOURCE']['DbQuery'])

    # Combine data if needed
    combined_data = pd.concat([csv_data, db_data])

    # Transform
    transformed_data = transform(combined_data)

    # Load
    load_csv(transformed_data, config['DESTINATION']['CsvFilePath'])
    load_db(transformed_data, config['DESTINATION']['DbConnectionString'], config['DESTINATION']['TableName'])
