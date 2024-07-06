class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 0

        def can(sp):
            hr = 0
            for i in range(len(piles)):
                hr += ceil(piles[i]/sp)
        
            return hr <= h
        
        while l + 1 < r:
            mid = (l+r)//2

            if can(mid):
                r = mid
            else:
                l = mid
        

        return r


        