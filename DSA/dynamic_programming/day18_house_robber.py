def rob(nums:list[int])->int:
    if len(nums)==1:
        return nums[0]
    dp=[0]*len(nums)
    dp[1]=max(nums[0],nums[1])
    for i in range(2,len(nums)):
        dp[i]=max(nums[i]+dp[i-2],dp[i-1])
    return dp[-1]
print(rob([1,9,8,7,3]))