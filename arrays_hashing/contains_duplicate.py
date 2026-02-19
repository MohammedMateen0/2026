def contains_duplicate(nums:list[int])->bool:
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_duplicate([1,3,2,4,2,5]))