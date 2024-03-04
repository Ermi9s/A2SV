class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []

        def backtrack(s):
            ans.append(sub[:])
            if len(sub) == len(nums):
                return 
            
            for i in range(s , len(nums)):
                sub.append(nums[i])
                backtrack(i+1)
                sub.pop()
                
        backtrack(0)
        return ans 





        