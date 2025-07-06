# Leetcode no 56 : Merge Intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        row = 0 
        while row < len(intervals) -1 :
            if intervals[row][1] >= intervals[row+1][0]:
                intervals[row][1] = max(intervals[row][1], intervals[row+1][1])
                del intervals[row+1]
            else :
                row += 1 
        
        return intervals
    

intervals =[[1,3],[2,6],[8,10],[15,18]]
merge = Solution()
print(merge.merge(intervals))

 