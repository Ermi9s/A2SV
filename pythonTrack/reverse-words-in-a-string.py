class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s.strip()

        temp = list(s.split())
        ans = []

        for i in temp[::-1]:
            ans.append(i)
        
        return " ".join(ans)


        