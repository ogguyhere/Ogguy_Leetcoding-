# Leetcode no 121 : Best Time to Buy and Sell Stock

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
            
            # else:  
                # max_profit = max(max_profit,price - min_price ) COMPLEXITY HIGH IN THIS 
                
        return max_profit
    
prices = [7,1,5,3,6,4]

obj = Solution()
print(obj.maxProfit(prices))