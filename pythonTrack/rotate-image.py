class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        transpose = []
        transpose[:] = zip(*matrix)
        matrix.clear()

        for i in transpose:
            matrix.append(list(i[::-1]))

    

        

            

