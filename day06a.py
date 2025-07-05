# Leetcode no 1 : Two Sum

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        result = []
        for i in range (length):
            for j in range (i+1, length):
                if nums[i] + nums[j] == target:
                    result.append(nums[i])
                    result.append(nums[j])
                    break
        
        return result
Kay = [3,2,4]
target = 6
obj = Solution()
print(obj.twoSum(Kay,target))