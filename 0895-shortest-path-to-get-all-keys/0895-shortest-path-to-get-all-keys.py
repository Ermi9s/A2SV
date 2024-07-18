class Solution:
    def shortestPathAllKeys(self, grid):
        m, n, count = len(grid), len(grid[0]), 0 

        stack, visited = [], set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] in "abcdef":
                    count += 1 
                if grid[i][j] == "@":
                    stack.append((i,j,"",0))
                    visited.add((i,j,""))

        while stack:
            x,y,keys,steps = stack.pop(0)

            if len(keys) == count:
                return steps

            for (nx,ny) in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]:
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#" and (nx,ny,keys) not in visited:
                    if grid[nx][ny] in ".@" or grid[nx][ny].lower() in keys:
                        stack.append((nx,ny,keys,steps+1))
                        visited.add((nx,ny,keys))
                    elif grid[nx][ny] in "abcdef":
                        stack.append((nx,ny,keys+grid[nx][ny],steps+1))
                        visited.add((nx,ny,keys))

        return -1