class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in costs:
            i.append(i[1]-i[0])

        sums = 0
        costs.sort(key = lambda x:x[2] , reverse = True)

        for i in range(len(costs)//2):
            sums += costs[i][0]
        
        for i in range(len(costs)//2, len(costs)):
            sums += costs[i][1]


        
        return sums
        
        

        