class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def isConnected(r1 , r2):
            for i in range(m):
                if grid[r1][i] and grid[r2][i]:
                    return True
            
            return False
        
        score = {}
        touched = defaultdict(set)
        ans = 0
        for i in range(n):
            score[i] = sum(grid[i])
            touched[i].add(i)

            for j in range(i-1 , -1 , -1):
                if isConnected(i , j) and j not in touched[i]:
                    score[i] += score[j]
                    touched[i] = touched[i].union(touched[j])
                    if score[j] > 1:
                        ans -= score[j]
               
            if score[i] > 1:
                ans += score[i]
        
        return ans


