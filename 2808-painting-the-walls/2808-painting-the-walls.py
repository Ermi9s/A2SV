class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
            n = len(cost)

            @cache
            def dfs(i, painted):
                if painted >= n: return 0
                if i >= n: return float('inf')
                return min(
                    dfs(i + 1, painted + time[i] + 1) + cost[i], # paint
                    dfs(i + 1, painted) # don't paint
                )

            return dfs(0, 0)