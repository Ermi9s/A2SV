class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_occ = [0] * 26

        def check(word):
            temp = [0] * 26

            for ch in word:
                ind = ord(ch) - ord('a')
                temp[ind] += 1
                max_occ[ind] = max(max_occ[ind] , temp[ind])
        
        for word in words2:
            check(word)
        
        def validate(word):
            temp = [0] * 26

            for ch in word:
                ind = ord(ch) - ord('a')
                temp[ind] += 1

            for i in range(26):
                if max_occ[i] > temp[i]:
                    return False
            
            return True
        
        ans = []

        for word in words1:
            if validate(word):
                ans.append(word)
        
        return ans