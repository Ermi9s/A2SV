class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(1,len(nums),2):
            for _ in range(nums[i-1]):
                ans.append(nums[i])
        

        return ans


        