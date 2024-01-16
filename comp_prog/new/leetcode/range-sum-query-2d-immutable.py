class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix

        for i in range(1):
            for j in range(1 , len(matrix[i])):
                self.mat[i][j] += self.mat[i][j - 1]
        
        for i in range(1 ,len(matrix)):
            for j in range(1):
                self.mat[i][j] += self.mat[i-1][j]
        
        for i in range(1, len(matrix)):
            for j in range(1 , len(matrix[0])):
                self.mat[i][j]= self.mat[i-1][j] + self.mat[i][j-1] - self.mat[i-1][j-1] + self.mat[i][j]
        
        for i in self.mat:
            i.append(0)
            
        self.mat.append([0]*len(matrix[0]))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        victum = self.mat[row1-1][col1 -1]
        d1= self.mat[row1 -1][col2]
        d2 = self.mat[row2][col1 - 1]

        ans = self.mat[row2][col2] - (d1 + d2) + victum

        return ans

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)