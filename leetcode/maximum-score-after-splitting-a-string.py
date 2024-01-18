class Solution:
    def maxScore(self, s: str) -> int:
        nums = [int(i) for i in s]
        l = 0
       
        run = 0
        maxi = 0
        total = sum(nums)
        for i in nums[:-1]:
            if i == 0:
                l += 1
            else:
                run += 1
            maxi = max(maxi , l + (total - run))
        
        return maxi