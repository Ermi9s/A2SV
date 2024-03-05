class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1, 10)]
        combo = []
        ans = []

        def backtrack(s):
            if len(combo) >= k and sum(combo) != n:
                return
            if len(combo) == k and sum(combo) == n:
                ans.append(combo[:])
                return 
        
            for i in range(s,len(nums)):
                combo.append(nums[i])
                backtrack(i+1)
                combo.pop()
        
        backtrack(0)

        return ans
            

