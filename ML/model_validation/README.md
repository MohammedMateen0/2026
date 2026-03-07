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
