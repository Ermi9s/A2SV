class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        cheker = set()
        for i in range(26):
            cheker.add(chr(i+97))
        for i in range(10):
            cheker.add(str(i))
        l = 0
        r = len(s) -1

        while l < r:  
            if s[l] not in cheker:
                l += 1
                continue
            if s[r] not in cheker:
                r -= 1
                continue

            if s[l] != s[r]:
                return False
            else:
                l+= 1
                r-= 1
        
        return True
            
            

