class DSU:
    def __init__(self , N):
        self.parent = {i : i for i in range(N+1)}
        self.size = {i : 1 for i in range(N+1)}

    def find(self,node):
        
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        
        return node
    
    def union(self, a, b):
        node1 = self.find(a)
        node2 = self.find(b)

        if node1 == node2:
            return
        
        if self.size[node1] < self.size[node2]:
            node1,node2 = node2,node1
        
        self.parent[node2] = node1
        self.size[node1] += self.size[node2]
    
    def isConnected(self, a , b):
        return not (self.find(a) == self.find(b))
    

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(start , graph):
            stk = [start]
            seen = set([start])

            while stk:
                node = stk.pop()

                for nbr in graph[node]:
                    if nbr not in seen:
                        stk.append(nbr)
                        seen.add(nbr)
   
            return len(seen)

        def check(ind):
            graph = defaultdict(list)
            indegree = defaultdict(int)

            for i in range(len(edges)):
                if i == ind:
                    continue

                graph[edges[i][0]].append(edges[i][1])
                indegree[edges[i][1]] += 1
       
            for node in range(1 , len(edges)+1):
                if not indegree[node] and (len(edges) == dfs(node , graph)):
                    return True
            
            return False
        
        for i in range(len(edges)-1 , -1 , -1):
            if check(i):
                return edges[i]
            