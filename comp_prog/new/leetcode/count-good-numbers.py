class Solution:
    store = {}
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5
        if n == 2:
            return 20
        
        if n in self.store:
            return self.store[n]
        else:
            if n % 2 == 1:

                self.store[n] = (self.countGoodNumbers(n//2 + 1) * self.countGoodNumbers(n//2))% (pow(10,9) + 7)
            else:
                self.store[n] = (self.countGoodNumbers(n-1) * 4)% (pow(10,9) + 7)
            
            return self.store[n]
    
        