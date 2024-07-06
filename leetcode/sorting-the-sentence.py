class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        sortedd = ["" for _ in range(len(lst))]
        
        for i in lst:
            sortedd[int(i[-1]) - 1] = i[:len(i)-1]
        
        return str(" ".join(sortedd))
        
        

        