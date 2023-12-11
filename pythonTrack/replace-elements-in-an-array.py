class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        index = {}
       

        for i,n in enumerate(nums):
            index[n] = i
            
        for op in operations:

            nums[index[op[0]]] = op[1]
            i = index.pop(op[0])
            index[op[1]] = i

        return nums
        


        
         
