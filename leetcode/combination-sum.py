class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combo = []

        def backtrack(s):
            if sum(combo) > target:
                return
            if sum(combo) == target:
                ans.append(combo[:])
                return 

            # print(combo) 
            for i in range(s , len(candidates)):
                combo.append(candidates[i])
                backtrack(i)
                combo.pop()
                
                


        backtrack(0)

        return ans

        