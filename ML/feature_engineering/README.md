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
## Day 11 — Feature Scaling

### Problem

Machine learning models can behave poorly when features have very different numeric ranges.

Example:

| Feature | Range            |
| ------- | ---------------- |
| Age     | 18–80            |
| Income  | 50,000–5,000,000 |

Distance-based and gradient-based models may incorrectly assume larger-scale features are more important.

---

### Solution: Feature Scaling

Feature scaling ensures that all features operate on a comparable numerical scale.

---

### Standardization (StandardScaler)

Standardization transforms data to have:

Mean = 0
Standard Deviation = 1

Formula:

z = (x − mean) / standard deviation

Implementation:

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Important rule:

* `fit()` only on training data
* `transform()` on both training and test data

This prevents **data leakage**.

---

### Min-Max Normalization (MinMaxScaler)

Scales values into the range:

0 → 1

Formula:

(x − min) / (max − min)

Example usage:

```python
from sklearn.preprocessing import MinMaxScaler
```

---

### When Scaling Is Necessary

Scaling is important for models relying on distance or gradients:

* Logistic Regression
* KNN
* SVM
* Neural Networks
* PCA

Scaling is generally **not required** for tree-based models:

* Decision Trees
* Random Forest
* XGBoost
* LightGBM

These models split using thresholds rather than distances.

---

### Key Takeaways

* Feature scaling prevents numerical dominance of large-range features.
* Always fit scalers on training data only.
* Preventing data leakage is critical for reliable model evaluation.

