# Day 5 — Evening Session

## SQL Window Functions → Pandas Translation

### 🎯 Objective

Translate SQL analytical functions into vectorized Pandas operations.

---

## 🔎 SQL Concept

Original SQL:

```sql
DENSE_RANK() OVER (
    PARTITION BY department
    ORDER BY salary DESC
)
```

This ranks salaries within each department.

---

## 🐼 Pandas Equivalent

```python
df["rank"] = df.groupby("department")["salary"].rank(
    method="dense",
    ascending=False
)
```

---

## 🧠 Concept Mapping

| SQL           | Pandas               |
| ------------- | -------------------- |
| PARTITION BY  | groupby()            |
| ORDER BY DESC | ascending=False      |
| DENSE_RANK()  | rank(method="dense") |

---

## 📊 Behavior Example

If department salaries are:

```
120000
90000
90000
80000
```

Dense ranking becomes:

| Salary | Rank |
| ------ | ---- |
| 120000 | 1    |
| 90000  | 2    |
| 90000  | 2    |
| 80000  | 3    |

No ranking gaps.

---

## ⏱ Complexity

Time: O(n) (vectorized operations)
Space: O(n)

---

## 🚀 Key Takeaway

Understanding analytical SQL allows seamless translation into Pandas.

This skill is critical for:

* Data Science roles
* Analytics engineering roles
* Finance and healthcare interviews
