class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        count = 0
        maxi = 0

        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            maxi = max(maxi,count)

        return maxi
            
            
            
        