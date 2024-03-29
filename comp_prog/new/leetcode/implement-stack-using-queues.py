class MyStack(object):

    def __init__(self):
        self.que = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)         
    def pop(self):
        """
        :rtype: int
        """
        return self.que.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.que[-1]
    def empty(self):
        """
        :rtype: bool
        """
        if self.que:
            return False
        return True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()