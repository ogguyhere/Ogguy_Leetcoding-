# Leetcode no 509 : Fibonacci Number 

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1 
        
        result = self.fib(n-1) + self.fib(n-2)
        
        return result 
    
obj = Solution ()
print (obj.fib(7))
            
            
                    
        