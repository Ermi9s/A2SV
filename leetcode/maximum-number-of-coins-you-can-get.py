class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        i = 0
        mine = 0
        while i != len(piles):
            piles.pop()
            mine += piles[-1]
            piles.pop()
            i += 1
        
        return mine

        