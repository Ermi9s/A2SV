class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] >= target:
                r -= 1
            elif nums[l] + nums[r] < target:
                count += len(nums[l:r])
                l += 1
        return count

                

        

            



        