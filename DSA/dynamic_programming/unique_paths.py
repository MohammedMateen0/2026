class Solution:
    def uniquePaths(self,m:int,n:int)->int:
        dp=[1]*n
        for _ in range(1,m):
            for c in range(1,n):
                dp[c]+=dp[c-1]
        return dp[-1]
    
if __name__=='__main__':
    solution=Solution()
    print(solution.uniquePaths(3,3))