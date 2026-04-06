from pyspark.sql import SparkSession
from pyspark.sql.functions import when

def run_spark_job():
    print("\n Starting PySpark Job...\n")

    # Step 1: Start Spark session
    spark = SparkSession.builder \
        .appName("Financial ETL") \
        .getOrCreate()

    # Step 2: Load CSV
    df = spark.read.csv("data/creditcard.csv", header=True, inferSchema=True)

    print("Data Loaded in Spark")
    df.printSchema()

    # Step 3: Transformation (same logic as pandas)
    df = df.withColumn(
        "amount_category",
        when(df["Amount"] > 1000, "High")
        .when(df["Amount"] > 100, "Medium")
        .otherwise("Low")
    )

    df = df.withColumn(
        "fraud_label",
        when(df["Class"] == 1, "Fraud")
        .otherwise("Normal")
    )

    print("\nTransformed Data (Spark):")
    df.select("Amount", "amount_category", "fraud_label").show(5)

    # Step 4: Count frauds
    fraud_count = df.filter(df["Class"] == 1).count()
    print(f"\nTotal Fraud Transactions: {fraud_count}")

    spark.stop()

if __name__ == "__main__":
    run_spark_job()