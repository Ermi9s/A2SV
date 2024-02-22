class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stk = []

        for token in tokens:
            if token in "+-*/":
                b = stk.pop()
                a = stk.pop()

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a * b
                else:
                    if a*b < 0 and a % b != 0:
                        result = a // b + 1
                    else:
                        result = a // b
                    

                stk.append(result)
            else:
                stk.append(int(token))

        return stk[0]
        """
        :type tokens: List[str]
        :rtype: int
        """
        