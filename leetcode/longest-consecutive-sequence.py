class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = sorted(list(set(nums)))
        count = 1
        maxCount = 1

        for i in range(1,len(temp)):
            if temp[i] - temp[i-1] == 1:
                count += 1
            else:
                count = 1
            maxCount = max(count, maxCount)
        
        return maxCount if nums else 0
        