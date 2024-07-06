class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stk = []
        zeros = []

        for i in nums:
            if i != 0:
                stk.append(i)
            else:
                zeros.append(i)
        stk.extend(zeros)
        nums.clear()
        nums[:] = stk


            
        

        