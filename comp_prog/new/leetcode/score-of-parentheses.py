class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stk = [0]

        for x in s:
            if x == "(":
                stk.append(0)
            else:
                v = stk.pop()
                stk[-1] += max(2*v,1)
        
        return stk.pop()

        