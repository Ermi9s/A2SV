class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        k = len(p)
        value = 0
        ans = []
        
        value = sorted(p)
        for i in range(len(s)-k+1):
            temp = sorted(s[i:k+i])

            if temp == value:
                ans.append(i)




        return ans  