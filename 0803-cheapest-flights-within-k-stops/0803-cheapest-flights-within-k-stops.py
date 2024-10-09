class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dp = [float('inf')]*(n+1)
        dp[src] = 0

        for i in range(k+1):
            temp = dp[:]
      
            for a,b,p in flights:
                temp[b] = min(temp[b] , dp[a] + p)
            
            dp = temp[:]
        
        
        return dp[dst] if dp[dst] != float('inf') else -1
        