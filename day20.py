from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = [0] * len(candies)
        for i in range (len(candies)):
            if (candies[i] + extraCandies >= maximum):
                result[i] = True
            else:
                result[i] = False
        return result
    


Lol = Solution()
print(Lol.kidsWithCandies((1,2,3,4,5),4))
