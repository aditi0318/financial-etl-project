import sqlite3

def load_data(df):
    print("\n Loading data into database...\n")

    # Step 1: Connect to SQLite DB
    conn = sqlite3.connect("data/financial.db")

    # Step 2: Load data into table
    df.to_sql("transactions", conn, if_exists="replace", index=False)

    print(" Data loaded into database successfully")

    # Step 3: Verify data
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transactions")
    count = cursor.fetchone()[0]

    print(f"\nTotal records in DB: {count}")

    # Step 4: Sample query
    print("\nSample Fraud Transactions:\n")

    query = """
    SELECT Amount, amount_category, fraud_label 
    FROM transactions 
    WHERE fraud_label = 'Fraud'
    LIMIT 5;
    """

    result = cursor.execute(query).fetchall()

    for row in result:
        print(row)

    conn.close()