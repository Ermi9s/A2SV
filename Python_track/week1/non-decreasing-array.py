class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        strike = 1
        prev_dif = 0

        for r in range(1,len(nums)):
            if nums[r] < nums[r-1]:
                strike -= 1

                #which one should i modify
                if nums[r-1] - nums[r] > prev_dif and r!=1:
                    nums[r] = nums[r-1]
                else:
                    nums[r-1] = nums[r]
            
            prev_dif = nums[r] - nums[r-1]
            
        
        if strike < 0:
            return False
        else:
            return True
           
            
        



        

# 1 2 3 4 1 6 7 8
     