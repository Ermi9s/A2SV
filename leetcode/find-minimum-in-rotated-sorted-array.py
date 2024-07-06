class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l + 1 < r:
            mid = (l+r)//2

            if nums[mid] > nums[l] or nums[mid] > nums[r]:
                if nums[l] < nums[r]:
                    r = mid
                else:
                    l = mid
            
            else:
                if nums[l] > nums[r]:
                    r = mid
                else:
                    l = mid   

        return min(nums[l],nums[r])
        