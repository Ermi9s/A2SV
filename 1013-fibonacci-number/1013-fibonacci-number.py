class Solution:
    def __init__(self):
        self.m = {}
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        if n not in self.m:
            self.m[n] = (self.fib(n-1) + self.fib(n-2))

        return self.m[n]
        