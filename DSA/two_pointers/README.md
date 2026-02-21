# Two Pointers Pattern — Day 3

## 📅 Overview

Day 3 focuses on mastering the Two Pointer technique, a critical O(n) optimization pattern used in FAANG-level interviews.

Instead of nested loops (O(n²)), two pointers reduce the search space intelligently using mathematical properties.

---

## 🧠 Problems Covered

### 1️⃣ Two Sum II (LeetCode 167)

* Constraint: Sorted input array
* Space: O(1)
* Time: O(n)
* Key Insight:
  Move left pointer to increase sum, move right pointer to decrease sum.

---

### 2️⃣ 3Sum (LeetCode 15)

* Time: O(n²)
* Steps:

  * Sort array
  * Fix index `i`
  * Apply Two Sum logic on remaining elements
* Critical Learning:

  * Skip duplicate `i`
  * Skip duplicate `left` and `right`
  * Early break when `nums[i] > 0` (target = 0 case)

---

### 3️⃣ Container With Most Water (LeetCode 11)

* Time: O(n)
* Formula:

  ```
  area = (right - left) × min(height[left], height[right])
  ```
* Key Insight:
  Move the pointer pointing to the shorter line, because the area is limited by the shorter height.

---

## 🔍 Core Pattern Understanding

Two Pointers works in different contexts:

| Problem Type   | Why It Works                       |
| -------------- | ---------------------------------- |
| Sorted Search  | Monotonic increase/decrease of sum |
| Triplet Search | Reduced nested search space        |
| Max Area       | Bottleneck height logic            |

---

## 🎯 Key Takeaways

* Eliminate unnecessary nested loops.
* Use mathematical reasoning to justify pointer movement.
* Duplicate handling is mandatory in 3Sum.
* Optimization pruning must be logically safe.

---

## 📈 Complexity Summary

| Problem                   | Time  | Space |
| ------------------------- | ----- | ----- |
| Two Sum II                | O(n)  | O(1)  |
| 3Sum                      | O(n²) | O(1)  |
| Container With Most Water | O(n)  | O(1)  |

---

## 🚀 Status

Two Pointer pattern successfully implemented and understood across multiple problem types.
