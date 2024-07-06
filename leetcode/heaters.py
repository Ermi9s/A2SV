class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        ans = 0

        heaters.sort()
        
        for i in houses:
            ind = bisect_left(heaters ,i)
            left = float('-inf') if ind == 0  else heaters[ind-1]
            right = float('inf') if ind == len(heaters) else heaters[ind]


            ans = max(ans, min((i - left) , (right - i)))
        
        return ans
        