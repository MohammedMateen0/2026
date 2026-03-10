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
