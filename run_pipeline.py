import os

print("\n Starting Full ETL Pipeline...\n")

# Step 1: Extract
os.system("python etl/extract.py")

# Step 2: Transform
os.system("python etl/transform.py")

# Step 3: Load
os.system("python etl/load.py")

# Step 4: Spark
os.system("python spark/spark_job.py")

# Step 5: SQL Analysis
os.system("python sql/analysis.py")

print("\n Pipeline Completed Successfully!\n")