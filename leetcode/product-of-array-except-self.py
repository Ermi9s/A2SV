class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right = [1]
        left = [1]
        n = len(nums)
        for i in range(n):
            left.append(left[-1]*nums[i])
            right.append(right[-1]*nums[n-i-1])
        right[:] = right[::-1]
        ans =[0] * n

  
        for i in range(n):
            ans[i] = left[i] * right[i+1]
        
        return ans