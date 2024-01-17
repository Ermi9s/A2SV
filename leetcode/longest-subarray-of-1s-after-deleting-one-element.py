class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Zcount = 0
        l = 0
        r = 0
        win = 0

        while r < len(nums):
            if nums[r] == 0:
                Zcount += 1

            while Zcount > 1:
                if nums[l] == 0:
                    Zcount -= 1
                l += 1

            win = max(win , r - l + 1)
            r += 1
        
        return win - 1
