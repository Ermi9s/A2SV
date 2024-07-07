class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        empty = 0

        while numBottles:
            ans += numBottles
            n = numBottles
            numBottles = (numBottles+empty)//numExchange
            empty = (n+empty)%numExchange
            
        
        return ans

        