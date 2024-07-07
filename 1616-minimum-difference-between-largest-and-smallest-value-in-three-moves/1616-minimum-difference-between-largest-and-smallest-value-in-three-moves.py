class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5: return 0
        nums.sort()
        
        def check(a , b):
            return abs(a - b)

        return min(check(nums[0], nums[-4]), check(nums[1], nums[-3]), check(nums[2], nums[-2]), check(nums[3], nums[-1]))
        