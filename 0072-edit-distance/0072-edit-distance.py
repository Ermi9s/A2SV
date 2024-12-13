class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i , j):
            if i == len(word1) or j == len(word2):
                return max(len(word1) - i, len(word2) - j)

            return min(dp(i+1, j)+1,  dp(i+1, j+1) + int(word1[i] != word2[j]), dp(i , j+1)+1) 
        
        return dp(0, 0)
            
        