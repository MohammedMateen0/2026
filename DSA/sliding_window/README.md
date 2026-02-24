# Day 4 — Sliding Window & String Encoding

## 📅 Overview

Day 4 focuses on advanced Sliding Window logic and robust string encoding techniques used in system design and backend services.

---

## 🧠 Problems Covered

### 1️⃣ Best Time to Buy and Sell Stock (LeetCode 121)

**Goal:**
Find the maximum profit by buying and selling once.

**Approach:**
Track the minimum price seen so far and compute profit at each step.

**Core Logic:**

* Maintain `minimum` price.
* At each price, calculate `price - minimum`.
* Update maximum profit.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

**Key Insight:**
At every step, we ask:

> If I sell today, what is the best profit possible given the cheapest price seen so far?

---

### 2️⃣ Encode and Decode Strings (LeetCode 271 Pattern)

**Goal:**
Convert a list of strings into a single string and decode it back safely.

**Approach:**
Use length-prefixed encoding.

**Encoding Format:**

```
length#string
```

Example:

```
["Hello", "world"] → "5#Hello5#world"
```

**Why This Is Safe:**
Even if a string contains `#`, the decoder reads the exact number of characters using the length prefix.

**Time Complexity:** O(n)
**Space Complexity:** O(n)

---

## 🔍 Core Concepts Learned

| Concept                | Application                  |
| ---------------------- | ---------------------------- |
| Sliding Window         | Eliminating nested loops     |
| Minimum Tracking       | Efficient profit calculation |
| Two Pointer Parsing    | String decoding              |
| Length-Prefix Encoding | Safe message serialization   |

---

## 🎯 Key Takeaways

* Sliding Window can be simplified into min/max tracking.
* Encoding schemes must be delimiter-safe.
* Index management is critical in string parsing problems.
* Clean variable naming improves readability and interview quality.

---

## 🚀 Status

Sliding Window pattern reinforced.
String encoding/decoding implemented using robust length-prefix method.
