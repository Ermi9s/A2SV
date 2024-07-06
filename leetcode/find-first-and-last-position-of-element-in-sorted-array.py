class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1 ,-1]

        ans = [-1 , -1]
        def leftOcc(num):
            l = -1
            r = len(nums)-1

            while l+1 < r:
                mid = (l+r)//2

                if nums[mid] < target:
                    l = mid
                else:
                    r = mid
            
            return r
        
        def rightOcc(num):
            l = 0
            r = len(nums)

            while l+1 < r:
                mid = (l+r)//2

                if nums[mid] <= target:
                    l = mid
                else:
                    r = mid
            
            return l
        
        if nums[leftOcc(target)] == target and nums[rightOcc(target)]==target:
            return [leftOcc(target) , rightOcc(target)]
        else:
            return ans

        