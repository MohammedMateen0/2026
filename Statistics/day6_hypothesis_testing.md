# Day 6 — Hypothesis Testing for Model Deployment

## 📅 Evening Session Overview

Understanding statistical significance is essential for ML roles in finance and pharma industries.

Scenario:

* Model A Accuracy = 90%
* Model B Accuracy = 92%

Question:
Can we deploy Model B?

---

## 🧠 Key Concepts

### 1️⃣ Null Hypothesis (H₀)

There is no real difference between Model A and Model B.
The 2% improvement is due to random variation.

---

### 2️⃣ Alternative Hypothesis (Hₐ)

Model B truly performs better than Model A.

---

### 3️⃣ P-Value

The probability of observing the measured improvement (or more extreme) assuming the null hypothesis is true.

---

## 📊 Decision Rule

| P-Value | Conclusion                                         |
| ------- | -------------------------------------------------- |
| < 0.05  | Reject Null Hypothesis (Statistically Significant) |
| ≥ 0.05  | Fail to Reject Null (Not Significant)              |

---

## 🔎 Interpretation Examples

* **p-value = 0.01**
  → Strong evidence Model B is better.

* **p-value = 0.20**
  → Improvement could be random noise. Not enough evidence to deploy.

---

## 🚀 Industry Importance

In production environments:

* Accuracy increase alone is not enough.
* Statistical testing validates improvement.
* Decisions must be backed by evidence, not intuition.

This level of reasoning differentiates a Data Scientist from a script runner.
