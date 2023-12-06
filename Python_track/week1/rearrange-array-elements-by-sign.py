class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        negs = []
        result = []

        for n in nums[::-1]:
            if n < 0:
                negs.append(n)
        
        for i in nums:
            if i >= 0:
                result.append(i)
                result.append(negs.pop())
        
        return result

        

        