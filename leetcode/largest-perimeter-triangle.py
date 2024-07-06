class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()

        for i in range(-1 , 1-len(nums), -1):
            m = i - 1
            f = i - 2
            
            if nums[i] + nums[m] > nums[f] and nums[m] + nums[f] > nums[i] and nums[i] + nums[f] > nums[m]:
                return (nums[i] + nums[m] + nums[f])

        return 0
              
        
      
                


        