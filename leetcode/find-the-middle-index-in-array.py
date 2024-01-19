class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        suf = [nums[-1]]

        for i in range(1,len(nums)):
            suf.append(suf[-1] + nums[len(nums) -1 -i])

        suf[:] = suf[::-1]

        sums = 0

        for i,n in enumerate(nums):
            sums += n
            if sums == suf[i]:
                return i
        return -1