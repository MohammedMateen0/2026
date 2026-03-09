# Day 12 — Cross Validation

## Why Cross Validation?

A single train-test split can produce misleading results because the test set may contain unusually easy or difficult samples.

Cross-validation evaluates the model across multiple data splits.

---

## K-Fold Cross Validation

Dataset is divided into K folds.

Example with 5 folds:

Train on 4 folds
Test on 1 fold

This repeats 5 times so every fold becomes the test set once.

Final performance is the average of all scores.

---

## Stratified K-Fold

Used for classification problems.

Ensures class distribution remains consistent in every fold.

Example:

If dataset contains:

95% normal
5% fraud

Each fold maintains this same ratio.

---

## Key Takeaways

* Prevents evaluation randomness
* Provides more robust performance estimates
* Essential for reliable ML model validation
## Day 13 — Model Evaluation Metrics

Machine learning models must be evaluated using more than just accuracy, especially when dealing with imbalanced datasets.

### Confusion Matrix

A confusion matrix summarizes prediction results.

| Actual / Predicted | Positive            | Negative            |
| ------------------ | ------------------- | ------------------- |
| Positive           | True Positive (TP)  | False Negative (FN) |
| Negative           | False Positive (FP) | True Negative (TN)  |

---

### Precision

Formula:

Precision = TP / (TP + FP)

Meaning:

When the model predicts positive, how often is it correct?

High precision means fewer false alarms.

---

### Recall (Sensitivity)

Formula:

Recall = TP / (TP + FN)

Meaning:

Out of all actual positive cases, how many were correctly identified.

High recall means fewer missed cases.

---

### F1 Score

F1 is the harmonic mean of Precision and Recall.

F1 = 2 * (Precision * Recall) / (Precision + Recall)

This metric is especially useful for **imbalanced datasets**.

---

### Key Insight

Accuracy alone can be misleading in problems such as:

* Fraud detection
* Medical diagnosis
* Spam detection

In these cases, metrics such as **Precision, Recall, and F1 Score** provide better insight into model performance.
