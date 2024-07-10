class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []

        def check(st):
            return st == st[::-1]
        
        def backtrack(ind):            
            if ind >= len(s):
                ans.append(path[:])
                return 
            
            for i in range(ind , len(s)+1):
                if s[ind:i] and check(s[ind:i]):
                    path.append(s[ind:i])
                    backtrack(i)
                    path.pop()

        
        backtrack(0)
        return ans
        