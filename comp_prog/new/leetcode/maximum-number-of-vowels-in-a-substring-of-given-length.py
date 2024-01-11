class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vs = {'a','e','i','o','u'}
        v = 0
        c = 0
    
        for i in s[:k]:
            if i in vs:
                v += 1
            else:
        
              c += 1

        ans = v
        l = 0
        r = l + k

        while r < len(s):
            if s[l] in vs:
                v -= 1
            else:
                c -= 1

            if s[r] in vs:
                v += 1  
            else:
                c += 1 

            ans = max(ans , v)  
            l += 1
            r += 1
      
        return ans