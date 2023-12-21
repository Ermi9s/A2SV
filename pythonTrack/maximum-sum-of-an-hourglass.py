class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        def magic(arr,i,j):
            sums = (arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1]) + arr[i][j] + (arr[i+1][j+1] + arr[i+1][j] + arr[i+1][j-1])
            return sums
        
        maxi = 0
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[i])-1):
                maxi = max(maxi , magic(grid,i,j))
        
        return maxi

        
    

        