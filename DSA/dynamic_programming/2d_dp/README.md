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