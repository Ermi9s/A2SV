class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        board = [['.' for _ in range(n)]for _ in range(n)]
        col = set()
        ld = set()
        rd = set()

        def backtrack(r):
            if r == n:
                temp = [''.join(i[:]) for i in board]
                ans.append(temp)
                return 
            
            # print(board)
            for i in range(n):
                if i in col or (r-i) in ld or (i+r) in rd:
                    continue
                
                board[r][i] = 'Q'
                col.add(i)
                ld.add(r-i)
                rd.add(r+i)

                backtrack(r+1)

                board[r][i] = '.'
                col.remove(i)
                ld.remove(r-i)
                rd.remove(r+i)
        
        backtrack(0)
        return ans



            



        