class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }

        ans = []
        lst = [int(i) for i in digits]
        path = []

        def backtrack(s):
            if len(path) == len(lst):
                if path:
                    ans.append(''.join(path))
                return 
            
            for i in mp[lst[s]]:
                # if s+1 < len(lst):
                path.append(i)
                backtrack(s+1)
                path.pop()
        
        backtrack(0)

        return ans


        