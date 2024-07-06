class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        mp = {ch: 1 for ch in 'qwertyuiop'}
        mp.update({ch: 2 for ch in 'asdfghjkl'})
        mp.update({ch: 3 for ch in 'zxcvbnm'})

        ans = []

        for word in words:
            test = set()
            for i in word:
                test.add(mp[i.lower()])

            if len(test) == 1:
                ans.append(word)

        return ans
            


