class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        sums = 0
        count = 0
        for i in range(len(costs)):
            sums += costs[i]
            if sums > coins:
                break
            count += 1
        return count
        



        