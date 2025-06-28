# Leetcode 231 : Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 :
            return False
        
        element = 0
        while (element == 0):
            if n == 1:
                return True
            element = n % 2
            n = n/ 2
            

        return False 
        
obj = Solution()
print(obj.isPowerOfTwo(16))