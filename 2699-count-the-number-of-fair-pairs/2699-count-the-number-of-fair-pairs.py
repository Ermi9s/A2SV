class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        ans = 0
        nums.sort()
        arr = []
        # print(nums)
        for i in range(len(nums)):
            lb = bisect_left(arr , lower - nums[i])
            ub = bisect_right(arr , upper - nums[i])

            arr.append(nums[i])

            # print(nums[i] , lb,ub)
            ans += (ub - lb)
        
        return ans
        