class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        count = defaultdict(int)

        l = 0
        r = 0
        ans = float('-inf')
        while r < len(nums):
            count[nums[r]] += 1

            while count[nums[r]] > 1 and l < r:
                count[nums[l]] -= 1
                l += 1
            
            ans = max(ans , sum(nums[l:r+1]))
            r += 1
            
        return ans