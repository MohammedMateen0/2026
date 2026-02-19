from typing import List

class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for key, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], key]
            seen[value] = key
        raise ValueError("No solutions found")

    def contains_duplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count1, count2 = {}, {}

        for cher in s:
            count1[cher] = count1.get(cher, 0) + 1
        for cher in t:
            count2[cher] = count2.get(cher, 0) + 1

        return count1 == count2


if __name__ == "__main__":
    solver = Solution()
    print(solver.two_sum([1,2,3,4,5,6,7,8], 9))
    print(solver.contains_duplicate([1,2,3,4,5,6,7,7,6]))
    print(solver.is_anagram("anagram", "nagaram"))
