# Day 10 — Trees & Recursion (DFS Fundamentals)

## 📅 Overview

Day 10 marks the transition from linear data structures to hierarchical structures.

Binary Trees require recursive reasoning and understanding of the call stack.

---

## 🧠 Problems Covered

### 1️⃣ Invert Binary Tree (LeetCode 226)

Swaps the left and right child of every node in the tree.

**Approach:**

* Base Case: If node is None → return None
* Swap children
* Recursively invert left and right subtrees

**Time Complexity:** O(n)
**Space Complexity:** O(h) where h = tree height

---

### 2️⃣ Maximum Depth of Binary Tree (LeetCode 104)

Finds the longest path from root to leaf.

**Recursive Formula:**

depth = 1 + max(depth(left), depth(right))

**Base Case:** If node is None → depth = 0

**Time Complexity:** O(n)
**Space Complexity:** O(h)

---

## 🔁 DFS Traversal Types

| Traversal | Order               |
| --------- | ------------------- |
| Preorder  | Root → Left → Right |
| Inorder   | Left → Root → Right |
| Postorder | Left → Right → Root |

For Binary Search Trees:

* Inorder traversal returns sorted order.

---

## 📊 Recursion Stack Insight

* Balanced Tree → Space O(log n)
* Skewed Tree → Space O(n)

Understanding recursion stack depth is critical for technical interviews.

---

## 🚀 Key Takeaways

* Base case discipline is essential.
* Every recursive tree problem follows:

  * Base Case
  * Recursive Call
  * Return aggregation
* Trees test multi-state reasoning and stack awareness.

This session builds foundational depth for advanced tree problems.
## Day 11 — Breadth First Search (Level Order Traversal)

### Problem

Binary Tree Level Order Traversal (LeetCode 102)

Return node values level by level.

Example:

```
    3
   / \
  9   20
     /  \
    15   7
```

Output:

[[3], [9, 20], [15, 7]]

---

### Approach

This problem uses **Breadth-First Search (BFS)**.

Instead of recursion, BFS uses a **Queue (FIFO)**.

Implementation uses `collections.deque` for efficient O(1) operations.

Algorithm:

1. Initialize queue with root node
2. While queue is not empty
3. Determine number of nodes at current level
4. Process those nodes
5. Add their children to queue

---

### Important Engineering Detail

Avoid using a normal Python list as a queue.

Bad approach:

queue.pop(0) → O(n)

Correct approach:

```python
from collections import deque
queue.popleft()  # O(1)
```

---

### Complexity

Time Complexity: O(n)
Space Complexity: O(n)

Maximum queue size equals the **width of the tree**.

