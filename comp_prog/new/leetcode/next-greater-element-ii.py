class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ch = {(i , nums[i]):-1 for i in range(len(nums))}

        stk = []
        n = len(nums)
        for i in range(n*2):
            while stk and nums[i%n] > stk[-1][1]:
                temp = stk.pop()
                ch[temp] = nums[i%n]

            stk.append((i%n , nums[i%n]))
        
        for i in range(len(nums)):
            nums[i] = ch[(i , nums[i])]
        
        return nums
        






        