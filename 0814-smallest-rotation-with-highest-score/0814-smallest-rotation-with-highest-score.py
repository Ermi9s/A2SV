class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [0] * len(nums)
        for i, v in enumerate(nums):
            low = (i+1)% len(nums)
            high = (i - v + len(nums)+1)%len(nums)
            diff[low] +=1  
            diff[high] -=1 
            if low >= high:
                diff[0] +=1
        
        current = 0
        maxi = 0
        idx = 0
        for i, v in enumerate(diff):
            current += v
            if current>maxi:
                maxi = current
                idx = i
        return idx