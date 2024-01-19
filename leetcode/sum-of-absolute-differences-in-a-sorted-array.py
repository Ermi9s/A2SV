class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = [nums[0]]
        suf = [nums[-1]]
        ans = [0] * len(nums)

        for i in range(1,len(nums)):
            pre.append(nums[i] + pre[-1])
            suf.append(suf[-1] + nums[len(nums)- 1 - i])
        
        suf[:] = suf[::-1]

        n = len(nums) - 1
        for i in range(len(nums)):
            ans[i] = ((suf[i] - nums[i]) - (nums[i] * (n - i))) + ((i*nums[i]) - (pre[i] - nums[i]))

        return ans