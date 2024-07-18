class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n = len(grid)

        def getValidMoves(i, j):
            validMoves = []
            for dx, dy in moves:
                x, y = i + dx, j + dy
                if x >= 0 and y >= 0 and y < n and x < n:
                    validMoves.append((x, y))
            return validMoves

        def dfs(i, j, id):
            if grid[i][j] == 0 or grid[i][j] > 1: return 0
            grid[i][j] = id
            return 1 + sum(dfs(x, y, id) for x,y in getValidMoves(i, j))
        
        
        areaMap = {0: 0}
        id = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    areaMap[id] = dfs(i, j, id)
                    id += 1

        maxArea = max(areaMap.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    islandsJoined = set(grid[x][y] for x, y in getValidMoves(i, j))
                    area = 1 + sum(areaMap[id] for id in islandsJoined)
                    maxArea = max(area, maxArea)

        return maxArea