# Day 10 — Advanced Feature Engineering

## 📅 Overview

Day 10 Evening focuses on transforming raw features into mathematically meaningful representations for machine learning models.

Topics covered:

* Log Transformation (handling skewed distributions)
* Target Encoding (handling high-cardinality categorical variables)
* Data Leakage awareness

---

## 🔹 Log Transform

### Problem

Financial features such as salary and property price are often right-skewed due to extreme outliers.

### Solution

Apply:

```python
np.log1p(df["price"])
```

### Why log1p?

* Handles zero safely
* Compresses extreme values
* Stabilizes variance
* Helps linear regression assumptions

### Model Sensitivity

* Linear models benefit strongly from log transforms.
* Tree-based models (XGBoost, LightGBM) are less sensitive because they split using thresholds.

---

## 🔹 Target Encoding

### Problem

High-cardinality categorical variables (e.g., zip codes) create too many columns with one-hot encoding.

### Solution

Replace each category with the mean target value of that category.

Example:

```python
df.groupby("zip_code")["price"].mean()
```

### Warning: Data Leakage

Naive target encoding uses the full dataset and leaks target information into training.

Correct approach:

* Use K-Fold target encoding
* Compute encoding only on training folds

---

## 📊 Key Takeaways

* Feature engineering is conditional, not automatic.
* Transformations must match model assumptions.
* Leakage awareness is critical in production ML.
* High-cardinality handling separates junior and senior ML engineers.

This session strengthens production-level ML thinking.
