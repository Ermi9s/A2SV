class Solution:
    def maxIncreaseKeepingSkyline(self, nums: List[List[int]]) -> int:
        rowMax = []
        colMax = []

        for i in nums:
            rowMax.append(max(i))
        
        for j in range(len(nums[0])):
            maxi = nums[0][j]
            for i in range(len(nums)):
                if nums[i][j] > maxi:
                    maxi = nums[i][j]

            colMax.append(maxi)

        inc = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                inc += ((min(rowMax[i] , colMax[j])) - nums[i][j])
        
        return inc


                


        