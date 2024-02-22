class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort(reverse = True)
        ans = 0
        for k in range(len(nums) - 2):
            l = k+1
            r = len(nums)-1
            
            while r > l:
                if nums[r] + nums[l] > nums[k]:
                    ans += (r-l)
                    l += 1
                else:
                    r -= 1
                
        return ans
        
        

        