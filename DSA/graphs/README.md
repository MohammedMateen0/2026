# Graph Algorithms

Graphs represent relationships between nodes. Many interview graph problems appear as **2D grid traversal problems**.

## Day 14 – Number of Islands

Problem: Count the number of islands in a grid of land (`1`) and water (`0`).

### Approach

1. Iterate through every cell in the grid.
2. When land (`1`) is found, increment island count.
3. Run DFS to explore the entire island.
4. Convert visited land to water (`1 → 0`) to avoid revisiting.

### DFS Sink Technique

Instead of maintaining a separate visited set, the grid itself is modified:

`grid[r][c] = "0"`

This prevents counting the same island multiple times.

### Time Complexity

O(m × n)

Each cell is visited at most once.

### Space Complexity

O(m × n) worst case recursion stack.
# Day 15 – Multi-Source BFS (Rotting Oranges)

## Problem

Implement the solution for **Rotting Oranges (LeetCode 994)** using **Breadth-First Search (BFS)**.

In this grid problem:

* `0` → empty cell
* `1` → fresh orange
* `2` → rotten orange

Every minute, any fresh orange adjacent (up, down, left, right) to a rotten orange becomes rotten.

The task is to determine the **minimum number of minutes required until no fresh orange remains**.

If some fresh oranges can never rot, return `-1`.

---

## Key Concept – Multi-Source BFS

Unlike standard BFS (which starts from one node), this problem starts BFS from **multiple sources simultaneously**.

All rotten oranges act as **initial infection sources**.

### Algorithm Steps

1. Traverse the entire grid.
2. Count the number of fresh oranges.
3. Add all rotten oranges to a queue.
4. Perform BFS using the queue:

   * Process the grid level by level.
   * Each BFS level represents **1 minute**.
5. Convert adjacent fresh oranges to rotten and add them to the queue.
6. Continue until no fresh oranges remain or the queue becomes empty.

---

## BFS Layer Simulation

Example:

Initial grid

2 1 1
1 1 0
0 1 1

Minute 0
Initial rotten oranges start the infection.

Minute 1
Adjacent oranges become rotten.

Minute 2
Next layer of oranges becomes rotten.

Continue until no fresh oranges remain.

Final result: **4 minutes**


## Complexity Analysis

**Time Complexity**

O(m × n)

Every cell in the grid is visited at most once.

**Space Complexity**

O(m × n)

Worst-case queue size when the grid contains many oranges.

---

## Key Learning

This problem introduces the **multi-source BFS pattern**, which is commonly used in:

* infection spread simulations
* shortest time propagation problems
* grid-based graph traversal


## Day 16 — Course Schedule (Cycle Detection in Directed Graph)

This problem models task dependencies using a directed graph.

### Problem

Given a number of courses and prerequisite pairs `[a, b]`, determine if all courses can be completed.

`[a, b]` means course `b` must be completed before course `a`.

### Key Idea

If the graph contains a **cycle**, the courses cannot be completed.

Example cycle:

0 → 1 → 2 → 0

### Solution Approach

1. Build an adjacency list.
2. Track node states using three markers:

   * 0 = unvisited
   * 1 = visiting
   * 2 = visited
3. Run DFS on every course.
4. If we encounter a node already in state `1`, a cycle exists.

### Time Complexity

O(V + E)

V = number of courses
E = number of prerequisite edges

### Concept Learned

Cycle detection in directed graphs using DFS.
