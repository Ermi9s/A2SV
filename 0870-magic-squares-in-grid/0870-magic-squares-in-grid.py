class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check(x,y):
            i = x-2
            j = y-2
            t = x+y-2

            d1 = []
            d2 = []
            h = []
            s = set()
            for l in range(i , x+1):
                sums = 0
                for r in range(j , y+1):
                    if grid[l][r] in s or grid[l][r] > 9 or grid[l][r] < 1:
                        return False
                    s.add(grid[l][r])
                    sums += grid[l][r]
                    if l-x == r-y:
                        d1.append(grid[l][r])
                    if l+r == t:
                         d2.append(grid[l][r])
                if h and h[-1] != sums:
                    return False
                h.append(sums)

            v = []
            for r in range(j , y+1):
                sums = 0
                for l in range(i , x+1):
                    sums += grid[l][r]
                
                if v and sums != v[-1]:
                    return False
                v.append(sums)
            
            # print(v , h , d1 , d2)
            if sum(d1) == sum(d2) == v[-1] == h[-1]:
                return True
            

            return False

        ans = 0
        for i in range(2 , len(grid)):
            for j in range(2 , len(grid[0])):
                if check(i,j):
                    ans += 1
        
        return ans