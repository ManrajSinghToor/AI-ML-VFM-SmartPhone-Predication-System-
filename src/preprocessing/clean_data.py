def clean_data(df):

    print("\nCleaning Dataset...")

    df = df.drop_duplicates()

    numeric_columns = [
        "RAM",
        "Storage",
        "Front Camera",
        "Back Camera",
        "Price"
    ]

    for col in numeric_columns:

        df[col] = df[col].fillna(
            df[col].median()
        )

    return df