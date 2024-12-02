class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = sentence.split()
        k = len(searchWord)

        for i in range(len(lst)):
            if len(lst[i]) < k:
                continue
            
            if lst[i][:k] == searchWord:
                return i+1
        
        return -1
            


        