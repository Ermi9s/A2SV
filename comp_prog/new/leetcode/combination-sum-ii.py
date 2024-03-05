class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            check = set()
            candidates.sort()
            ans = []
            combo = []
            flag = [False]
            def backtrack(s):
                
                if sum(combo) > target:
                    return
              
                if sum(combo) == target and tuple(combo[:]) not in check:
                    ans.append(combo[:])
                    check.add(tuple(combo[:]))

                # print(combo) 
                x = 0
                for i in range(s , len(candidates)):
                    if candidates[i] != x: 
                        combo.append(candidates[i])
                        backtrack(i+1)
                        x = combo.pop()

            
            backtrack(0)
            return ans
    