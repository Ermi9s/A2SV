from fractions import Fraction
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = Counter()
        ans = 0

        for a,b in rectangles:
            ans += count[a/b]
            count[a/b] += 1
        
        return ans

        
        