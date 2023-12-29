class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        op = 0
        l = 0
        for i in range(len(nums)-1, 0 , -1):
            l += 1
            if nums[i] > nums[i-1]:
                op += l
        
        return op
