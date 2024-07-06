class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [(0 , -1),(0 , 1) , (-1 , 0) , (1 , 0)]
        n = len(matrix)
        m = len(matrix[0])

        def inrange(r , c):
            return 0 <= r < n and 0 <= c < m
        
        outdegree = defaultdict(int)

        que = deque()
        seen = [[0 for _ in range(m)] for _ in range(n)]
        path = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                for a,b in dirs:
                    x = i+a
                    y = j+b
                    if inrange(x , y) and matrix[x][y] > matrix[i][j]:
                        outdegree[(i , j)] += 1

        for i in range(n):
            for j in range(m):
                if outdegree[(i , j)] == 0:
                    que.append((i , j))
                    seen[i][j] = 1

        while que:
            x,y = que.popleft()
            path[x][y] += 1

            for a,b in dirs:
                i = a + x
                j = b + y

                if inrange(i , j) and matrix[i][j] < matrix[x][y]:
                    outdegree[(i , j)] -= 1
                    path[i][j] = max(path[i][j] , path[x][y])
                    if not seen[i][j] and outdegree[(i , j)] == 0:
                        que.append((i , j))
                        seen[i][j] = 1

        max_val = float('-inf')
        for row in path:
            max_val = max(max_val , max(row))
        
        return max_val
        
        