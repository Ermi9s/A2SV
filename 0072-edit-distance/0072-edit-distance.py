class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[(m+n)]*(m+1) for _ in range(n+1)]
        dp[-1][-1] = 0

        for i in range(n, -1 , -1):
            for j in range(m , -1 , -1):
                x = i+1
                y = j+1

                if x <= n:
                    dp[i][j] = min(dp[i][j], dp[x][j] + 1)
                
                if y <= m:
                    dp[i][j] = min(dp[i][j], dp[i][y] + 1)
                
                if  x <= n and y  <= m:
                    dp[i][j] = min(dp[i][j] , dp[x][y] + int(word1[i] != word2[j]))
        

        return dp[0][0]




        



        