class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = set(nums)
        actual = set(range(0,len(nums)+1))
       

        for i in actual:
            if i not in snums:
                return i
        