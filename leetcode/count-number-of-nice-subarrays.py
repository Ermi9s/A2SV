class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0
        count = 0
        ans = 0

        l = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                count = 0
                odd += 1
            
            while odd == k:
                if nums[l] % 2 != 0:
                    odd -= 1
                l+= 1
                count += 1
            
            ans += count
 
        return ans
        



