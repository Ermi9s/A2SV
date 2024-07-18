class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        stack = []

        op = ""
        num = ""
        for char in expression:
            if char in "!&|":
                op = char
                continue
            elif char in "tf":
                num += char
                continue
            elif char == ",":
                continue

            if char == "(":
                stack.append([op, num])
                op, num = "", ""
            else:   # char == ")"
                pre_op, pre_num = stack.pop()
                num = pre_num + self.cal(pre_op, num)

        return True if num == "t" else False

    def cal(self, op, num):
        if "t" in num and op == "|":
            return "t"
        if "f" not in num and op == "&":
            return "t"
        if num == "f" and op == "!":
            return "t"

        return "f"




