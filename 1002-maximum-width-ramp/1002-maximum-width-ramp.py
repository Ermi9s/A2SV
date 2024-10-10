class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stk = []
        for i in range(len(nums)):
            if not stk or nums[stk[-1]] > nums[i]:
                stk.append(i)
        
        ans = 0
        for i in range(len(nums)-1 , 0 , -1):
            while stk and nums[stk[-1]] <= nums[i]:
                ans = max(ans , i - stk[-1])
                stk.pop()
        

        return ans








        