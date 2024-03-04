class Solution:
    def combine(self, n: int, k: int , s = 1) -> List[List[int]]:
        ans = []
        def backtrack( s , path):
            if len(path) == k:
                ans.append(path[:])
                return 
            
            for i in range(s , n+1):
                path.append(i)
                backtrack(i+1 , path)
                path.pop()
        
        backtrack(1 , [])
        return ans

            
        
