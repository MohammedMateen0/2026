from typing import List
class Day_6:
    def binary_search(self,nums:list[int],target:int)->bool:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return True
        return False
    def search_matrix(matrix:list[list[int]],target:int)->bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n=len(matrix[0])
        left=0
        right=m*n-1
        while left<=right:
            mid=left+(right-left)//2
            row=mid//n
            col=mid%n
            value=matrix[row][col]
            if value==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
            return False
if __name__=="__main__":
    solver=Day_6

    print(solver.search_matrix([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,15,16]],8))
    print(solver.binary_search([1,2,3,4,5,6,7,8,9,11],8))