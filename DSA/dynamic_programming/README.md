Day 18 — Dynamic Programming (1D DP)

Dynamic Programming optimizes recursion by storing previously computed results.

Problems Covered

1. Climbing Stairs
2. House Robber

---

Climbing Stairs

Number of ways to reach step "n" using 1 or 2 steps.

Recurrence

dp[n] = dp[n-1] + dp[n-2]

This follows the Fibonacci pattern.

---

House Robber

Maximize money without robbing adjacent houses.

Recurrence

dp[i] = max(nums[i] + dp[i-2], dp[i-1])

---

Key Concepts

- Overlapping subproblems
- Optimal substructure
- State transition

---

Optimization

Space optimized to O(1) using two variables instead of full DP array.

---

Time Complexity

O(n)