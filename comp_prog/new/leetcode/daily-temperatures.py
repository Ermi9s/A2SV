class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        ch = {(i , nums[i]):0 for i in range(len(nums))}

        stk = []

        for i in range(len(nums)):
            while stk and stk[-1][1] < nums[i]:
                temp = stk.pop()
                ch[temp] = (i - temp[0])
            
            stk.append((i , nums[i]))
        
        for i in range(len(nums)):
            nums[i] = ch[(i , nums[i])]
        
        return nums
        