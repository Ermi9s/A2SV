class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        grid =  [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = min(rowSum[i] , colSum[j])
                rowSum[i] -= grid[i][j]
                colSum[j] -= grid[i][j]
        
        return grid


        