def two_sum(nums:list[int],target:int)->list[int]:
    seen={}
    for key,numm in enumerate(nums):
        complement=target-numm
        if complement in seen:
            return [seen[complement],key]
        seen[numm]=key
    raise ValueError("NO solution found")
print(two_sum([2,3,4,5,6,7,8,9],9))