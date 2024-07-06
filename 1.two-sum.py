#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = []
        nums = [[nums[i] , i] for i in range(len(nums))]
        nums.sort()
        
        while l < r:
            if nums[l][0] + nums[r][0] > target:
                r -= 1
            elif nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                ans.append(nums[l][1])
                ans.append(nums[r][1])
                l += 1
                r -= 1
                

        return ans
        
# @lc code=end

