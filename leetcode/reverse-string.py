class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s):
            if len(s) == 1:
                return s 
            if len(s) == 2:
                return s[::-1]
            
            left = reverse(s[:len(s)//2])
            right = reverse(s[len(s)//2:])

            return right + left
        
        s[:] = reverse(s)

