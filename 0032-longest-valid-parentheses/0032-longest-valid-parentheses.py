class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        mx = 0
        for i in range(len(s)):
            # print(stk)
            if s[i] == "(":
                stk.append(i)
            elif stk and s[i] == ")" and s[stk[-1]] == "(":
                stk.pop()
                if stk:
                    mx = max(mx , i - stk[-1])
                else:
                    mx = max(mx , i+1)
            else:
                stk.append(i)
        
        return mx


        