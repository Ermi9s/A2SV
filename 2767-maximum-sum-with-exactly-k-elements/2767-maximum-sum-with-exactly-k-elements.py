class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        bound = mx + k - 1

        all_ =  (bound*(1 + bound))//2
        sub = (mx*(mx - 1))//2

    
        return all_ - sub