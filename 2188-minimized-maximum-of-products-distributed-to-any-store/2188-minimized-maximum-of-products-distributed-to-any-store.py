class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def check(num):
            res = 0
            for i in range(len(quantities)):
                res += (quantities[i] + num-1)//num
            
            return res <= n
        
        l = 0
        r = sum(quantities)+1

        while l+1 < r:
            mid = (l+r)//2

            if check(mid):
                r = mid
            else:
                l = mid
        
        return r
        
        