# Leetcode no 1337 : The K Weakest Rows in a Matrix

import heapq 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        
        for i in range(len(mat)) :
            count = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    count += 1
            
            heapq.heappush(heap,(count, i))
            
        return [heapq.heappop(heap)[1] for _ in range(k)]
    
# # another solution not mine but is 100% beat 
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

#         row = []

#         res = []

#         for i in range(len(mat)):

#             row.append((sum(mat[i]), i))

#         row.sort()

#         for i in range(k):

#             res.append(row[i][1])

#         return res
        