class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0 
        r = 0
        count = 0
        while r < len(s):
            if s[r] == '0':
                count += (r - l)
                l += 1
            r += 1
        
        return count



