## Day 17 — Word Search (Backtracking)

This problem demonstrates **Backtracking**, a variation of Depth-First Search where the algorithm must restore state after exploring a path.

### Problem

Given an `m x n` board of characters and a target word, determine if the word exists in the grid.

Rules:

* The word must be constructed from sequentially adjacent cells.
* Cells can be used **only once per path**.

### Approach

1. Iterate through each cell in the grid.
2. Start DFS when the first letter matches.
3. Mark the current cell as visited using `'#'`.
4. Recursively search in four directions.
5. Restore the original letter after recursion (Backtrack).

### Backtracking Pattern

choose → explore → unchoose

### Time Complexity

O(N * 4^L)

N = number of grid cells
L = length of the word

### Key Concept

State restoration ensures other DFS paths can reuse the same cell later.
