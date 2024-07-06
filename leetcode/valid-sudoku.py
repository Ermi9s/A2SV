class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            horiz = set()
            for j in i:
                if j in horiz and j != ".":
                    return False
                horiz.add(j)

        for i in range(9):
            verti = set()
            for j in range(9):
                if board[j][i] in verti and board[j][i] != ".":
                    return False
                verti.add(board[j][i])
    
        for k in range(0, 9, 3):
            for l in range(0, 9, 3):
                collect = set()
                for i in range(k, k+3):
                    for j in range(l, l+3):
                        if board[i][j] != "." and board[i][j] in collect:
                            return False
                        collect.add(board[i][j])
                    
            
        return True

        


        