# Day 7 — Class Imbalance & SMOTE

## 📊 Scenario

Fraud detection dataset:

* 99,000 legitimate transactions
* 1,000 fraud transactions

Model achieved 99% accuracy but missed all fraud cases.

---

## 🧠 Why This Happens

* Dataset is highly imbalanced.
* Model predicts the majority class ("Legitimate") every time.
* Accuracy becomes misleading.
* Recall for fraud = 0%.

---

## 🔧 Solution: SMOTE

SMOTE (Synthetic Minority Over-sampling Technique):

* Generates synthetic minority samples using nearest neighbors.
* Prevents overfitting caused by simple duplication.
* Forces the model to learn minority patterns.

---

## 🎯 Key Metrics for Imbalanced Data

* Recall
* Precision
* F1-score
* PR-AUC

Accuracy alone is insufficient.
