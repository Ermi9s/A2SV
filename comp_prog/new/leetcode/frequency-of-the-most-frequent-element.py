class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        l = 0
        r = 0
        sums = 0
        win = 0
        while r < len(nums):
            var = (r-l+1)*nums[l]
            sums += nums[r]

            if l <= r and var - sums > k:
                sums -= nums[l]
                l += 1
                
            win = max(win , (r-l+1))        
            r += 1
        
        return win