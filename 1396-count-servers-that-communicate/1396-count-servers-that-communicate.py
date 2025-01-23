class DSU:
    def __init__(self,size):
        self.parent = {i : i for i in range(size+1)}
        self.size = {i:1 for i in range(size+1)}
    

    def find(self,node):

        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        
        return node
    

    def union(self, a , b):
        pa = self.find(a)
        pb = self.find(b)

        if pa == pb:
            return 
        
        if self.size[pa] < self.size[pb]:
            pa,pb = pb,pa
        
        self.parent[pb] = pa
        self.size[pa] += self.size[pb]
    
    def isConnected(self, a , b):
        return self.find(a) == self.find(b)


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def isConnected(r1 , r2):
            for i in range(m):
                if grid[r1][i] and grid[r2][i]:
                    return True
            
            return False
        
        un = DSU(n+1)
    
        score = {}
        ans = 0
        for i in range(n):
            score[i] = sum(grid[i])
        
            for j in range(i-1 , -1 , -1):
                if isConnected(i , j) and not un.isConnected(i , j):
                    score[i] += score[j]
                    if score[j] > 1:
                        ans -= score[j]
                    un.union(i , j)
               
            if score[i] > 1:
                ans += score[i]
        
        return ans


