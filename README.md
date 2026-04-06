# 💳 Financial ETL Pipeline

## 📌 Overview

This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** for financial transaction data, integrated with **PySpark processing** and **SQL-based analysis**.

The pipeline simulates a real-world **data engineering workflow**, focusing on data ingestion, transformation, storage, and analytical processing.

---

## ⚙️ Tech Stack

- Python (Pandas, NumPy)
- SQLite (Relational Database)
- PySpark (Distributed Data Processing)
- SQL (Data Analysis)
- Power BI (Planned for Visualization)

---

## 🏗️ Pipeline Architecture
Raw CSV Data
↓
Extract (Python)
↓
Transform (Cleaning + Feature Engineering)
↓
Load (SQLite Database)
↓
PySpark Processing
↓
SQL Analysis


---

## 📂 Project Structure
financial-etl-project/
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── spark/
│ └── spark_job.py
│
├── sql/
│ └── analysis.py
│
├── data/ # Ignored (contains raw & processed data)
├── run_pipeline.py # Main pipeline runner
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🔄 ETL Pipeline Details

### 🔹 Extract
- Reads raw financial transaction data from CSV
- Performs initial validation

### 🔹 Transform
- Removes duplicate records
- Handles missing values
- Performs data type corrections
- Creates derived features:
  - `amount_category` → Low / Medium / High
  - `fraud_label` → Fraud / Normal

### 🔹 Load
- Loads processed data into **SQLite database (`financial.db`)**
- Ensures structured schema for analysis

---

## ⚡ PySpark Processing

- Loads processed data into Spark DataFrame
- Performs scalable transformations
- Generates insights on transaction behavior and fraud patterns

---

## 📊 SQL Analysis

- Total transaction count
- Fraud vs Normal distribution
- Average transaction amount by category
- High-value transaction insights

---

## ▶️ How to Run

### 1. Clone the repository
```
git clone https://github.com/aditi0318/financial-etl-project.git
cd financial-etl-project
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Run the complete pipeline
```
python run_pipeline.py
```

### 4. (Optional) Run individual modules
```
python etl/extract.py
python etl/transform.py
python etl/load.py
python spark/spark_job.py
python sql/analysis.py
```

## 📌 Dataset

Due to size limitations, the dataset is not included in this repository.

Download here:
https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## 🧹 Cleaned Dataset

The dataset has been cleaned and transformed using the ETL pipeline in this project.

To view or use the processed (cleaned) dataset, you can download it from:
https://www.kaggle.com/datasets/aditi318/creditcard-dataset

## 🎯 Key Features
- Modular ETL pipeline design
- End-to-end data processing workflow
- Feature engineering for financial data
- Integration with PySpark for scalable processing
- SQL-based analytical insights

## 🚀 Future Enhancements
- Power BI dashboard for visualization
- Workflow orchestration using Apache Airflow
- Cloud deployment (AWS S3 + Redshift)
- Real-time data streaming pipeline

## 👩‍💻 Author

Aditi Jha

