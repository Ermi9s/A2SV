class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        base = {chr(ord('a') + i):0 for i in range(26)}
        temp = {chr(ord('a') + i):0 for i in range(26)}
        ans = 0
        if len(s1) > len(s2):
            return False
        
        for i in s1:
            base[i] += 1
        
        k = len(s1)
        for i in s2[:k]:
            temp[i] += 1

        for l in range(len(s2) - k):
            if base == temp:
                return True

            temp[s2[l]] -= 1
            temp[s2[l+k]] += 1
        

        return base == temp



        
        