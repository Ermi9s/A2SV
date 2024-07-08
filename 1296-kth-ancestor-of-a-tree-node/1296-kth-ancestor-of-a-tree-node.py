class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.n = n
        self.LOG = 0
        self.depth = [0 for _ in range(n)]
        graph = defaultdict(list)

        for i in range(1 , n):
            graph[parent[i]].append(i)
        
        stk = [0]
        while stk:
            node = stk.pop()
            for nbr in graph[node]:
                stk.append(nbr)
                self.depth[nbr] = self.depth[node] + 1
        
        while 1 << self.LOG <= n:
            self.LOG += 1

        self.pre = [[0 for _ in range(self.LOG)] for _ in range(n)]

        for i in range(n):
            self.pre[i][0] = parent[i]
            if i != 0:
                self.depth[i] = self.depth[parent[i]] + 1

        for j in range(1 , self.LOG):
            for i in range(n):
                self.pre[i][j] = self.pre[ self.pre[i][j-1] ][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        if k > self.depth[node]:
            return -1

        for i in range(self.LOG):
            if 1 << i & k != 0:
                node = self.pre[node][i] 
        
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)