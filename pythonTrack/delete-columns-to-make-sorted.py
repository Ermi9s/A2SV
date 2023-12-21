class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        alphabet = {}
        for i in range(26):
            alphabet[chr(ord('a')+i)] = i + 1
        deleted = 0


        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if alphabet[strs[i][j]] < alphabet[strs[i - 1][j]]:
                    deleted += 1
                    break
        
        return deleted


        