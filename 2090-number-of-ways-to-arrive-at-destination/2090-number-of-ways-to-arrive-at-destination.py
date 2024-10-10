class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        dp = [float('inf')]*n
        dp[0] = 0
        ways = [Counter() for _ in range(n)]
        ways[0][0] = 1
        mod=10**9+7
        

        for _ in range(n-1):
            temp = dp[:]

            for a,b,w in roads:
                if temp[b] > dp[a] + w:
                    temp[b] = dp[a] + w
                    ways[b]=Counter()
                    s=0
                    for val in ways[a].values():
                        s+=val
                    ways[b][a] =s%mod


                elif temp[b] == dp[a]+w:
                    s=0
                    for val in ways[a].values():
                        s+=val
                    ways[b][a] = s%mod

                a,b=b,a
                if temp[b] > dp[a] + w:
                    temp[b] = dp[a] + w
                    ways[b]=Counter()
                    s=0
                    for val in ways[a].values():
                        s+=val
                    ways[b][a] =s%mod

                elif temp[b] == dp[a]+w:
                    s=0
                    for val in ways[a].values():
                        s+=val
                    ways[b][a] = s%mod

            dp=temp[:]
        s=0
        for val in ways[n-1].values():
            s+=val
        # print(dp)
        # print(ways)
        return s%mod

        
                