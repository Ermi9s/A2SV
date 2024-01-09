class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        alpha = {chr(ord("a") + i):0 for i in range(26)}
        beta = {chr(ord("a") + i):0 for i in range(26)}
        
        w = len(p)
        ans = []
        def helper(dicto , ind):
            if dicto == alpha:
                ans.append(ind)

        for i in p:
            alpha[i] += 1
        for i in s[:w]:
            beta[i] += 1
        if alpha == beta:
            ans.append(0)
        
        for l in range(1,len(s) - w + 1):
            beta[s[l-1]] -= 1
            beta[s[l+w -1]] += 1
            helper(beta,l)
        
        return ans
            

        


        
        
        