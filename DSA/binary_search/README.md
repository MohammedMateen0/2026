# Day 6 — Binary Search (Divide and Conquer)

## 📅 Morning Session Overview

Day 6 focuses on mastering **Binary Search**, reducing search complexity from O(n) to O(log n).

Binary search is mandatory when data is sorted. Using a linear scan on sorted data is considered inefficient in top-tier interviews.

---

## 🧠 Problems Covered

### 1️⃣ Binary Search (LeetCode 704)

**Goal:**
Search for a target value inside a sorted array.

**Core Logic:**

* Initialize `left = 0`, `right = len(nums) - 1`
* Use `while left <= right`
* Compute midpoint safely:

```id="1hj39k"
mid = left + (right - left) // 2
```

* Adjust search space based on comparison.

**Time Complexity:** O(log n)
**Space Complexity:** O(1)

---

### 2️⃣ Search a 2D Matrix (LeetCode 74)

**Problem Insight:**
The matrix behaves like a single sorted 1D array.

Instead of flattening physically (which increases space complexity),
we simulate flattening mathematically.

**Index Mapping:**

```id="78kduo"
row = mid // n
col = mid % n
```

Where:

* `n` = number of columns

**Search Range:**

```id="m8r0zx"
left = 0
right = m * n - 1
```

**Time Complexity:** O(log(m*n))
**Space Complexity:** O(1)

---

## 🔍 Engineering Takeaways

* Always use binary search for sorted data.
* Avoid unnecessary extra space.
* Understand index mapping deeply.
* Use overflow-safe midpoint formula.

---

## 🚀 Interview Signal

Using binary search correctly demonstrates:

* Algorithmic optimization awareness
* Mathematical reasoning
* Clean boundary handling
* Strong problem-solving discipline
