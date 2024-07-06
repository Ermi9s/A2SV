class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        maxi = nums[0]

        for i in range(1 ,len(nums)):
            sums = max(nums[i] , sums + nums[i])
            maxi = max(sums , maxi)
        
        return maxi
        