class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        n = len(s)
        ans = [' ' for _ in range(n)]

        for pos,ind in enumerate(indices):
            ans[ind] = s[pos]
        
        return ''.join(ans)

