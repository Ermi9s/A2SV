class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score_right = nums.count(1)
        score_left = 0

        maxi = score_left + score_right
        ans = [0]
        for r in range(1,len(nums)+1):
            l = r - 1
            if nums[l] == 0:
                 score_left += 1
            elif nums[l] == 1:
                score_right -= 1


            if maxi == (score_left + score_right):
                ans.append(r)
            elif (score_left + score_right) > maxi:
                maxi = (score_left + score_right)
                ans = []
                ans.append(r)

        
      
        return ans



        