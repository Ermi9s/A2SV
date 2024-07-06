class Solution:
    def opo(self,ch):
        if ch == 1:
            return 0
        else:
            return 1
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if (k - 1) % 2 == 0:
            return self.kthGrammar((n-1) ,( k//2 + k%2))
        else:
            return self.opo(self.kthGrammar((n-1) , ( k//2 + k%2)))



        