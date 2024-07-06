class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans =  float('inf')

        l = 0
        sums = 0
        for r in range(len(nums)):
            sums += nums[r]
            while sums >= target:
                ans = min(r-l+ 1 , ans)
                sums -= nums[l]
                l += 1
                
        
        return ans if ans !=  float('inf') else 0
        
        

        