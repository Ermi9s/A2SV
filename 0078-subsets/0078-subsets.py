class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mels = [[]]
        for i in range(len(nums)):
            temp = []
            for st in mels:
                temp.append(st[:] + [nums[i]])
            mels += temp
        return mels