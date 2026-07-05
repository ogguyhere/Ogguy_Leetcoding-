class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total = max(len(word1), len(word2))
        word1len = len(word1)
        word2len = len(word2)
        result = ""
        for i in range(total):
            if(i < word1len):
                result += word1[i]
            if (i < word2len):
                result += word2[i]

        return result
    

test = Solution()
print(test.mergeAlternately("abc", "pqr"))
