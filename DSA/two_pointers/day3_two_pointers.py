from typing import List
class TwoPointers:

    def two_sum_sorted(self,nums:list[int],target:int)->list[int]:
        left=0
        right=len(nums)-1
        while left<right:
            current_sum=nums[left]+nums[right]
            if current_sum>target:
                right-=1
            elif current_sum<target:
                left+=1
            else:
                return [left+1,right+1]
            
    def three_sum(self,nums:list[int])->list[list[int]]:
        nums.sort()
        result=[]
        right=len(nums)-1
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
        
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total <0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return result
    
    def max_area(self,height:list[int])->int:
        maximum_area=0
        left=0
        right=len(height)-1
        while left<right:
            area=(right-left)*min(height[left],height[right])
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        
            maximum_area=max(maximum_area,area)
        return maximum_area
if __name__=="__main__":
    solver=TwoPointers()
    print(solver.max_area([1,8,6,2,5,4,8,3,9,7]))
    print(solver.three_sum([-4,-7,-7,3,5,6,3,2,1]))       
    print(solver.two_sum_sorted([1,2,3,4,5,6,7,8,9],9))