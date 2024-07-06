class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        col = len(matrix)-1
        rw= len(matrix[0])-1

        if col == 0 or rw == 0:
            return True 


        for i in range(col,-1,-1):
            j = 0
            while i < col and j < rw:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j += 1
                i += 1
        for j in range(rw,-1,-1):
            i = 0
            while j < rw and i < col:
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
                j += 1
                i += 1
        
        
        return True 

            
        






    

    #[0][0] == [1][1] == [2][2]
    #[0][0] == [0+1][0+1]

        
        