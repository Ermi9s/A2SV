class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)//3
        result = []

        count = {}

        for i in nums:
            count[i] = count.get(i , 0) + 1
        
        for key in count.keys():
            if count[key] > n:
                result.append(key)
        
        return result
        