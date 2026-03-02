# Day 8 — Hyderabad Real Estate ETL Pipeline

## 📅 Overview

Day 8 focuses on building a production-ready ETL (Extract, Transform, Load) pipeline for a Hyderabad real estate dataset.

This pipeline is designed to simulate real-world data engineering workflows used in consulting firms, fintech companies, and pharma analytics teams.

The objective was to:

* Clean messy currency-formatted price columns
* Handle missing values intelligently
* Load transformed data into a SQLite database
* Implement logging for production-level monitoring

---

# 🏗 Architecture

The pipeline follows a standard ETL design pattern:

```
Raw CSV → Pandas Transformation → Data Cleaning → SQLite Database
```

Implemented inside the class:

```
HyderabadDataPipeline
```

---

# 📦 Components Implemented

## 1️⃣ Extract Layer

```python
def extract(self, file_path: str) -> pd.DataFrame
```

* Reads raw CSV file
* Uses try/except for safe execution
* Logs extraction status
* Avoids hardcoded file paths

---

## 2️⃣ Transform Layer

### 🔹 Currency Cleaning

```python
def clean_currency_columns(self, df: pd.DataFrame, column_name: str)
```

Handles messy formats such as:

* ₹45.0 L
* 1.2 Cr
* 75,00,000
* Missing values

### Transformation Logic

* Removes commas
* Detects unit:

  * `L` → multiplied by 100,000
  * `Cr` → multiplied by 10,000,000
* Converts to float
* Coerces invalid values to NaN
* Prevents crashes using safe parsing

This ensures numerical consistency for ML models.

---

### 🔹 Missing Value Handling

```python
def handle_missing_values(self, df: pd.DataFrame)
```

Instead of using `dropna()` blindly, the pipeline applies domain-aware imputation:

### Numerical Columns:

* Missing values filled with **median of that specific location**
* Preserves local price distribution
* Avoids distortion from global median

### Categorical Columns:

* Missing values replaced with `"Unknown"`

This reduces bias and maintains realistic data patterns.

---

## 3️⃣ Load Layer

```python
def load_to_sqlite(self, df: pd.DataFrame, table_name: str)
```

* Connects to local SQLite database
* Loads cleaned DataFrame using `to_sql`
* Replaces existing table safely
* Uses proper exception handling
* Closes database connection reliably

Database file example:

```
hyderabad_market.db
```

---

# 🧠 Engineering Enhancements

## Logging Integration

Replaced print statements with:

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

Benefits:

* Timestamped logs
* Clear execution tracking
* Production monitoring readiness
* MLOps alignment

---

# 📊 Why This Matters

This project demonstrates:

* Data cleaning beyond simple Pandas operations
* Handling Indian currency formats (Lakhs/Crores)
* Domain-aware missing value imputation
* Defensive programming
* Database integration
* Logging discipline
* Production mindset

This is significantly more realistic than notebook-only preprocessing.

---

# 🚀 Future Improvements

Planned enhancements:

* Add configuration file (YAML/JSON)
* Add validation layer (schema checks)
* Add unit tests (pytest)
* Containerize using Docker
* Deploy pipeline as scheduled job (Airflow or cron)

---

# 📁 Repository Structure

```
ML/
└── etl_pipeline/
    ├── hyderabad_pipeline.py
    └── README.md
```

---

# 🎯 Outcome

By completing Day 8:

* Transitioned from scripting to engineering
* Built a reusable ETL class
* Integrated transformation logic with database persistence
* Applied real-world data reasoning

This pipeline forms the foundation for future modeling work.
