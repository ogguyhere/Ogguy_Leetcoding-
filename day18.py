# Leetcode no 704 : Binary Search 

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0 
        end = len(nums) -1
        
        while start<= end :
            mid = (start+end)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid-1
            else :
                start = mid+1
        
        
        
        return -1
    
    
object = Solution()
nums = [-1,0,3,5,9,12]

print(object.search(nums,0))
        