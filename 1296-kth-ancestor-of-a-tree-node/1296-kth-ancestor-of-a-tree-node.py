class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        graph = defaultdict(list)
        for i in range(1 , n):
            graph[parent[i]].append(i)
        
        self.max_log = 0
        while 1 << self.max_log <= n:
            self.max_log += 1
        
        self.depth = [0 for _ in range(n)]
        self.ancestor = [[-1 for _ in range(self.max_log)] for _ in range(n)]

        stk = [0]
        while stk:
            node = stk.pop()
            
            self.ancestor[node][0] = parent[node]
            for level in range(1 , self.max_log):
                temp = self.ancestor[node][level-1]
                self.ancestor[node][level] = self.ancestor[temp][level-1]

            for nbr in graph[node]:
                self.depth[nbr] = self.depth[node]+1
                stk.append(nbr)
        

    def getKthAncestor(self, node: int, k: int) -> int:
        if self.depth[node] < k:
            return -1
        
        for i in range(self.max_log):
            if 1<<i & k:
                node = self.ancestor[node][i]
        
        return node

        


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)