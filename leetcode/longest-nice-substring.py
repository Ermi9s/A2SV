class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ans = [""]
        def solver(s):
            if len(s)==1:
                return
        
            cases = set(s)
            flag = True
            print(s)
            for i in range(len(s)):
                if s[i].swapcase() not in cases:
                    flag = False
                    break
                    
            if flag:
                ans.append(s)
            else:
                solver(s[:i])
                if i+1 < len(s):
                    solver(s[i+1:])
        
        solver(s) 
        ans.sort(key = len , reverse = True)

        return ans[0]
            


