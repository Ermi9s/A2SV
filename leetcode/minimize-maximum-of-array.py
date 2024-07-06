class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            nums[i] = int(ceil (sums/(i+1 )))
                
        
        return max(nums)

        