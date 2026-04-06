import pandas as pd

def transform_data(df):
    print("\n Starting Transformation...\n")

    # Step 1: Remove duplicates
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Duplicates removed: {initial_rows - len(df)}")

    # Step 2: Handle missing values (even if none exist)
    df = df.fillna(0)
    print("Missing values handled")

    # Step 3: Create amount category
    def categorize_amount(x):
        if x > 1000:
            return "High"
        elif x > 100:
            return "Medium"
        else:
            return "Low"

    df["amount_category"] = df["Amount"].apply(categorize_amount)

    # Step 4: Create fraud label
    df["fraud_label"] = df["Class"].apply(
        lambda x: "Fraud" if x == 1 else "Normal"
    )

    print("\n Transformation completed\n")

    print("Sample transformed data:\n")
    print(df[["Amount", "amount_category", "fraud_label"]].head())

    return df

