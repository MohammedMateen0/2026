# Day 7 — Linked Lists (Memory & Pointer Discipline)

## 📅 Overview

Day 7 transitions from array-based problems to node-based data structures.
Linked Lists test pointer manipulation and reference management.

---

## 🧠 Problems Covered

### 1️⃣ Reverse Linked List (LeetCode 206)

Reverses a singly linked list in-place.

**Core Logic:**

* Maintain three pointers:

  * `prev`
  * `curr`
  * `nxt`
* Reverse links one by one.

**Time Complexity:** O(n)
**Space Complexity:** O(1)

---

### 2️⃣ Merge Two Sorted Lists (LeetCode 21)

Merges two sorted linked lists into one sorted list.

**Engineering Trick:** Dummy Node Pattern

Steps:

* Create a dummy node.
* Maintain a tail pointer.
* Attach smaller node at each step.
* Append remainder.

**Time Complexity:** O(n + m)
**Space Complexity:** O(1)

---

## 🔍 Key Concepts Learned

* In-place pointer reversal
* Safe reference handling
* Dummy node pattern
* Edge-case management
* Traversal discipline

---

## 🚀 Interview Signal

Linked List problems test:

* Memory safety
* Pointer reasoning
* Ability to think without index access

Mastery here signals strong data structure fundamentals.
