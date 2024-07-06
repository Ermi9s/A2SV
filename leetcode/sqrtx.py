class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        l = 0
        r = x

        while l + 1 < r:
            mid = (l+r)//2

            if (mid*mid) > x:
                 r = mid
            else:
                l = mid


        return l




        