import pandas as pd
import os
from transform import transform_data
from load import load_data

def extract_data(file_path):
    # Step 1: Check if file exists
    if not os.path.exists(file_path):
        print(" File not found:", file_path)
        return None

    # Step 2: Read CSV file
    df = pd.read_csv(file_path)
    # Null value check
    print("\nNull values per column:\n", df.isnull().sum())
    print("\nTotal null values:", df.isnull().sum().sum())

    print(" Data loaded successfully\n")

    # Step 3: Basic validation checks
    print("Shape (rows, columns):", df.shape)
    print("Rows count:", len(df))
    print("Columns count:", len(df.columns))

    # Step 4: Column names
    print("\nColumns:\n", df.columns)

    # Step 5: Sample data checks
    print("\nFirst 5 rows:\n", df.head())
    print("\nLast 5 rows:\n", df.tail())

    # Step 6: Random sample (to validate data spread)
    print("\nRandom sample:\n", df.sample(5))

    return df


if __name__ == "__main__":
    file_path = "data/creditcard.csv"
    data = extract_data(file_path)

    if data is not None:
        transformed_data = transform_data(data)
        load_data(transformed_data)