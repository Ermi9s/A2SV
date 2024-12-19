class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()

        ans = []

        l = 0
        r = len(nums)-1

        while r  > l:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r -= 1
        
        if len(nums)%2:
            ans.append(nums[r])
        
        return ans
        