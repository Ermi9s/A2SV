class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        wor = [i for i in word]
        path = []
        pos = set()
        
        up = False
        bk = False
        fw = False
        dw = False

        def backtrack(i , j):
            nonlocal bk,up,dw,fw

            if path == wor:
                return True
            
            if (bk or fw or up or dw):
                return True

            if len(path) >= len(wor) and path != wor:
                return 

            if path and path[-1] != wor[len(path)-1]:
                return
 
            if (i , j) not in pos and i < len(board) and j < len(board[0]):
                path.append(board[i][j])

                pos.add((i,j))

                if path == wor:
                    return True
                # print(path)
                if i > 0 and (i-1,j) not in pos:
                    up = backtrack(i-1 , j)
                if j > 0 and (i,j-1) not in pos:
                    bk = backtrack(i , j - 1)
            
                if i < len(board) and (i+1 ,j) not in pos:
                    fw = backtrack(i+1 , j)
                if j < len(board[0]) and (i , j+1) not in pos:
                    dw = backtrack(i , j+1)
                    
                path.pop()
                pos.remove((i ,j))
                                        

            return (bk or fw or up or dw) 
        


        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i , j):
                    return True
        

        return False
        