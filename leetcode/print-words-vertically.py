class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        temp = s.split()
        mx = len(max(temp, key=len))
        mp = {}
        ans = ["" for _ in range(mx)]

        for i in range(mx):
            mp[i] = []
        
        for word in temp:
            for l in range(len(word)):
                mp[l].append(word[l])
                if l == len(word)-1:
                    for fil in range(l+1,mx):
                        mp[fil].append(" ")
        
        for i in mp.values():
            while i[-1] == " ":
                i.pop()
        for i,l in enumerate(mp.values()):
            ans[i] = ''.join(l)
            

        return ans
        




            


        