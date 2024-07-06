class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []

        for i in s:
            if stk and stk[-1] == '(' and i == ')':
                stk.pop()
                continue
            stk.append(i)
        
        return len(stk)

        