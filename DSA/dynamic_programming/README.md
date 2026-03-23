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