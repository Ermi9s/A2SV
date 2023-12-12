class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
     
        return count.most_common()[0][0] 


        