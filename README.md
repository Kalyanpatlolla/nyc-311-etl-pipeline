# 🚀 NYC 311 ETL Pipeline

End-to-end data engineering pipeline that extracts NYC 311 service request data from a public API, transforms it using Python & Pandas, and loads it into Google BigQuery for analysis.

---

## 📌 Project Overview

This project demonstrates a **production-style ETL pipeline**:

- Extracts real-time data from NYC Open Data API
- Cleans and transforms data using Pandas
- Stores processed data in Parquet format
- Loads structured data into BigQuery
- Performs SQL-based analytics

---

## 🏗️ Architecture

```
NYC Open Data API
        ↓
   Extract (Python)
        ↓
  Raw JSON (data/raw)
        ↓
  Transform (Pandas)
        ↓
Clean Parquet (data/processed)
        ↓
    Load (BigQuery)
        ↓
    SQL Analysis
```

---

## ⚙️ Tech Stack

- Python
- Pandas
- Google Cloud BigQuery
- SQL
- REST API
- Parquet

---

## 📂 Project Structure

```
nyc-311-etl-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── utils.py
│
├── queries/
│   ├── peak_hours_analysis.sql
│   ├── borough_distribution.sql
│   └── top_complaints_by_borough.sql
│
├── config.yaml
├── pipeline.py
├── requirements.txt
└── README.md
```

---

## 🔄 ETL Pipeline Steps

### 1️⃣ Extract
- Fetches NYC 311 data from API
- Saves raw JSON data

### 2️⃣ Transform
- Cleans missing values
- Formats columns
- Converts data types
- Stores optimized Parquet file

### 3️⃣ Load
- Uploads data into BigQuery table
- Dataset: `nyc_311_pipeline`
- Table: `service_requests`

---

## 📊 Sample Output

```sql
SELECT COUNT(*) AS total_rows
FROM `nyc-etl-project.nyc_311_pipeline.service_requests`;
```

Result:

```
total_rows = 100
```

---

## 📈 SQL Analysis

**Peak Hours Analysis**
- Identifies busiest complaint hours

**Borough Distribution**
- Shows complaint count per borough

**Top Complaints**
- Finds most frequent complaint types

---

## ▶️ How to Run

### 1. Clone Repo

```bash
git clone https://github.com/Kalyanpatlolla/nyc-311-etl-pipeline.git
cd nyc-311-etl-pipeline
```

### 2. Setup Environment

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Set Credentials

```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\kalya\gcp-key.json
set GCP_PROJECT_ID=nyc-etl-project
```

### 4. Run Pipeline

```bash
python pipeline.py
```

---

## ✅ Final Output

- Raw data stored locally (JSON)
- Clean data stored in Parquet
- Data loaded into BigQuery
- SQL queries generate insights

---

## 💡 Key Learnings

- Building modular ETL pipelines
- Working with real-world APIs
- Data cleaning with Pandas
- Cloud data warehousing (BigQuery)
- Writing analytical SQL queries

---

## 👤 Author

**Venkata Kalyan Reddy Patlolla**

