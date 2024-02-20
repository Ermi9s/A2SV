class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        nu = 1
        patch = 0
        r = 0

        while nu < n + 1:
         
            while nu < n + 1 and r < len(nums) and nu < nums[r] :
                patch += 1
                nu *= 2

            if r< len(nums) and nums[r] <= nu:
                nu += nums[r]
            
            if r >= len(nums):
                patch += 1
                nu *= 2

            r += 1
        
        return patch
        

        