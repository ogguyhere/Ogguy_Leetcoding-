# Leetcode no 41 : First Missing Positive 

from typing import List
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        pos_num = 1
        while pos_num in num_set:
            pos_num += 1 
            
        return pos_num
            
        
nums = [1,2,0]
obj = Solution()
print(obj.firstMissingPositive(nums))