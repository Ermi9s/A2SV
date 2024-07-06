class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [ [0 for _ in range(n)]for _ in range(m)]
        ans = m*n
        for i in guards:
            grid[i[0]][i[1]] = 5
            ans -= 1
        for i in walls:
            grid[i[0]][i[1]] = 7
            ans -= 1
        
        for g in guards:
            l = g[1]
            r = g[1]
            for i in range(g[1]-0):
                l -= 1

                if grid[g[0]][l] == 7 or grid[g[0]][l] == 5:
                    break
                elif grid[g[0]][l] == 0:
                    grid[g[0]][l] = 4
                    ans -= 1

            for _ in range((n - 1) - g[1]):
                r += 1

                if grid[g[0]][r] == 7 or grid[g[0]][r] == 5:
                    break
                elif grid[g[0]][r] == 0:
                    grid[g[0]][r] = 4
                    ans -= 1
            

        for g in guards:
            l = g[0]
            r = g[0]
            for _ in range(g[0]-0):
                l -= 1

                if grid[l][g[1]] == 7 or grid[l][g[1]] == 5:
                    break
                elif grid[l][g[1]] == 0:
                    grid[l][g[1]] = 4
                    ans -= 1

            for _ in range((m-1) - g[0]):
                r += 1

                if grid[r][g[1]] == 7 or grid[r][g[1]] == 5:
                    break

                elif grid[r][g[1]] == 0:
                    grid[r][g[1]] = 4
                    ans -= 1
            
        return ans









        