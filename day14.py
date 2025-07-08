# Leetcode no 3 : Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <1:
                return 0
        maxi = 1
        k = 0
        for i in range (len(s)):
            max2 = 1
            for j in range (k,i):
                if s[i] != s[j]:
                    max2 +=1
                else :
                    maxi = max(maxi, max2)
                    max2 = 0
                    k = j+1
            maxi= max(maxi,max2)
        
        return maxi
                
                
s =  "bbbbb"

strin = Solution()
print(strin.lengthOfLongestSubstring(s))