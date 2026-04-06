import sqlite3

def run_sql_analysis():
    print("\n Starting SQL Analysis...\n")

    # Step 1: Connect to database
    conn = sqlite3.connect("data/financial.db")
    cursor = conn.cursor()

    # Step 2: Total records
    cursor.execute("SELECT COUNT(*) FROM transactions")
    total = cursor.fetchone()[0]
    print(f"Total records: {total}")

    # Step 3: Fraud vs Normal count
    cursor.execute("""
        SELECT fraud_label, COUNT(*) 
        FROM transactions 
        GROUP BY fraud_label
    """)
    print("\nFraud vs Normal:")
    for row in cursor.fetchall():
        print(row)

    # Step 4: Average transaction amount by category
    cursor.execute("""
        SELECT amount_category, AVG(Amount) 
        FROM transactions 
        GROUP BY amount_category
    """)
    print("\nAverage Amount by Category:")
    for row in cursor.fetchall():
        print(row)

    # Step 5: Top 5 highest transactions
    cursor.execute("""
        SELECT Amount, fraud_label 
        FROM transactions 
        ORDER BY Amount DESC 
        LIMIT 5
    """)
    print("\nTop 5 Highest Transactions:")
    for row in cursor.fetchall():
        print(row)

    # Step 6: Fraud transactions only
    cursor.execute("""
        SELECT Amount, amount_category 
        FROM transactions 
        WHERE fraud_label = 'Fraud'
        LIMIT 5
    """)
    print("\nSample Fraud Transactions:")
    for row in cursor.fetchall():
        print(row)

    conn.close()
    print("\n SQL Analysis Completed\n")


if __name__ == "__main__":
    run_sql_analysis()