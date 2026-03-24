## Day 20 - Unbounded Knapsack (DP)

### Problem: Coin Change (LeetCode 322)

**Concept:**
- Unbounded DP (infinite choices)
- Minimize number of elements

**State:**
dp[a] = minimum coins needed for amount 'a'

**Transition:**
dp[a] = min(dp[a], 1 + dp[a - coin])

**Key Insight:**
Greedy fails → must explore all subproblems

**Complexity:**
- Time: O(amount × number of coins)
- Space: O(amount)

**Status:** ✅ Solved