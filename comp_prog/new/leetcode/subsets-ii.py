class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        check = set()
        ans = []
        sub = []

        def backtrack(s):
            if tuple(sub[:]) not in check:
                ans.append(sub[:])

            check.add(tuple(sub[:]))

            if len(sub) == len(nums):
                return 
            
            for i in range(s , len(nums)):
                sub.append(nums[i])
                backtrack(i+1)
                sub.pop()
        


        backtrack(0)
        return (ans)


        