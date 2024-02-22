class MinStack:

    def __init__(self):
        self.stk = []
        self.mstk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.mstk:
            self.mstk.append(val)
        elif self.mstk and self.mstk[-1] >= val:
            self.mstk.append(val)

    def pop(self) -> None:
        if self.stk:
            temp = self.stk.pop()

        if self.mstk and self.mstk[-1] == temp:
            self.mstk.pop()

    def top(self) -> int:
        return self.stk[-1]
        
    def getMin(self) -> int:
        return self.mstk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()