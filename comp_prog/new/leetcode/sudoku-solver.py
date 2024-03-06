class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        box = {(i,j):set() for i in range(3) for j in range(3)}
        col = {i:set() for i in range(9)}
        row = {i:set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(int(board[i][j]))
                    col[j].add(int(board[i][j]))
                    box[(i//3 , j//3)].add(int(board[i][j]))
        

        def place(i , j , n):
            board[i][j] = str(n)
            box[(i//3 , j//3)].add(n)
            row[i].add(n)
            col[j].add(n)

        def isvalid(i,j,n):
            return not(n in box[(i//3 , j//3)] or n in row[i] or n in col[j])  

        def remove(i,j,n):
            board[i][j] = "."
            box[(i//3 , j//3)].remove(n)
            row[i].remove(n)
            col[j].remove(n)


        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for n in range(1,10):
                            if isvalid(i,j,n):
                                place(i,j ,n)
                                # print(i,j ,n)
                             
                                if backtrack():
                                    # print(board)
                                    return True

                                remove(i,j,n)

                        return False

            return True
                
        backtrack()






        
        