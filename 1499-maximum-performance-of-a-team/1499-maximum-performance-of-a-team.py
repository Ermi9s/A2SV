class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        data = [ [ speed[i] , efficiency[i] ] for i in range(n)]
        data.sort(reverse = True , key = lambda x:x[1])
        selected = []
        speed_sum = 0
        performance = 0

        for i in range(n):
            min_eff = data[i][1]
            speed_sum += data[i][0]

            heappush(selected , data[i])

            if len(selected) > k:
                removed = heappop(selected)
                speed_sum -= removed[0]
            
            performance = max(performance , speed_sum*min_eff)

        return performance % (10**9 + 7)