class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stk = []
        ck = float('-inf')
        for i in nums[::-1]:
            if i < ck:
                return True
            while stk and i > stk[-1]:
                ck = stk.pop()
                
            stk.append(i)
        
        return False


        
        
            
            
        
        return False

        