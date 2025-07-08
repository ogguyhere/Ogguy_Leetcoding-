#Leetcode no 54 : Spiral Matrix

from typing import List

class Solution:
    def helpingfunction(self, matrix: List[List[int]], list : None) -> List[int]: 
        if not matrix or not matrix[0]:
            return list
        nums_cols = len(matrix[0])
        nums_rows = len(matrix)
        
        for i in range (nums_cols):
            list.append(matrix[0][i])
        for i in range (1,nums_rows):
            list.append(matrix[i][nums_cols-1])
        if nums_rows > 1:
            for i in range (nums_cols-2,-1,-1):
                list.append(matrix[nums_rows-1][i])     
        if nums_cols > 1: 
            for i in range(nums_rows-2,0,-1):
                list.append(matrix[i][0])    
            
        matrix = [row[1:-1] for row in matrix[1:-1]]
        if len(matrix) > 0 and len(matrix[0]) > 0:
            self.helpingfunction(matrix,list)
        
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        self.helpingfunction(matrix, result)
        return result
        
matrix =[[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12]]

spiral = Solution()
print(spiral.spiralOrder(matrix))