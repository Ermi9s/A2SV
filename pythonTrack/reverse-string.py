class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        temp = []

        while s:
            temp.append(s.pop())
        
        s[::] = temp
        