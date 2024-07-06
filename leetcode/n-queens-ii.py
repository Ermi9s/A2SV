class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        rd = set()
        ld = set()
        col = set()

        def backtrack(r):
            nonlocal ans
            if r == n:
                ans += 1
                return 
            
            for i in range(n):
                if i in col or (r-i) in ld or (r+i) in rd:
                    continue
                
                col.add(i)
                ld.add(r-i)
                rd.add(r+i)

                backtrack(r+1)

                col.remove(i)
                ld.remove(r-i)
                rd.remove(r+i)


        backtrack(0)
        return ans               



        