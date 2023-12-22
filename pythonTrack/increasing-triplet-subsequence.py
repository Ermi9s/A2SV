class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i = nums[0]
        j = float('inf')

        for n in nums:
            if n > j:
                return True
            elif n > i:
                j = n
     
            if n < i:
                i = n
       
        return False










