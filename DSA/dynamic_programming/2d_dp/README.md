## Day 19 - 2D Dynamic Programming

### 1. Unique Paths (LeetCode 62)
**Concept:**
- Grid-based DP
- Each cell depends on top and left

**Recurrence:**
dp[r][c] = dp[r-1][c] + dp[r][c-1]

**Complexity:**
- Time: O(m × n)
- Space: O(n) optimized

**Status:** ✅ Solved

---

### 2. Longest Common Subsequence (LeetCode 1143)

**Concept:**
- Sequence alignment DP
- Compare two strings with decisions

**Recurrence:**
- Match → dp[i][j] = 1 + dp[i-1][j-1]
- No match → dp[i][j] = max(dp[i-1][j], dp[i][j-1])

**Complexity:**
- Time: O(m × n)
- Space: O(n) optimized

**Status:** ✅ Solved
# DAY 21
# 🧠 Problem Core

We are transforming:

```
word1 → word2
```

Allowed operations:

* Insert
* Delete
* Replace

👉 Goal: **minimum operations**

---

## ⚙️ State Definition

Let:

* `dp[i][j]` = minimum operations to convert
  `word1[:i] → word2[:j]`

---

## 🧱 Base Case Initialization

Converting to/from empty string:

* Delete all characters:
* Insert all characters:

```text
dp[i][0] = i
dp[0][j] = j
```

---

## 🔁 State Transition

### Case 1: Characters match

dp[i][j] = dp[i-1][j-1]

👉 No cost

---

### Case 2: Characters don’t match

dp[i][j] = 1 + \min(dp[i][j-1],\ dp[i-1][j],\ dp[i-1][j-1])

Where:

* Insert → `dp[i][j-1]`
* Delete → `dp[i-1][j]`
* Replace → `dp[i-1][j-1]`

---

---

## 🔍 Example

```python
word1 = "horse"
word2 = "ros"
```

Operations:

```
horse → rorse (replace h → r)
rorse → rose (delete r)
rose → ros (delete e)
```

Answer = **3**

---

## ⚡ Complexity

* Time: **O(m × n)**
* Space: **O(m × n)**

---

