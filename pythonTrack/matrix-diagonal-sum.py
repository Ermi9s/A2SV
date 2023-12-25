class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        left = 0
        right = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i + j == len(mat[i])-1 and i - j == 0:
                    right -= mat[i][j]
                if i + j == len(mat[i])-1:
                    right += mat[i][j]
                if i - j == 0:
                    left += mat[i][j]
        
        return left + right 
        