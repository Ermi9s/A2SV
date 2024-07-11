class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ')':
                stack.append(char)
            else:
                substring = ""
                while stack[-1] != '(':
                    substring = substring + stack.pop()
                stack.pop()

                stack.extend(substring)
        return "".join(stack)






        