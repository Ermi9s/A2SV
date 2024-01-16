class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        count = 0
        zer = 0
        if 1 not in nums and k == 0:
            return 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k-= 1
            if k < 0 and l < r:
                if nums[l] == 0:
                    k += 1
                l += 1
            count = max(count,r - l+1)
        return count
        
        