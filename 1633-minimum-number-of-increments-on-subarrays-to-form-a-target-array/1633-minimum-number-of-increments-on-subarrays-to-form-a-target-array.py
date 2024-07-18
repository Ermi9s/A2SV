class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        stack = []

        for x in target:

            if not stack:
                stack.append(x)
                ans += x
                continue

            
            if stack[-1] < x:
                ans += x - stack[-1]
                stack.append(x)

            else:
                while stack and stack[-1] > x:
                    stack.pop()

                stack.append(x)

        return ans
        