class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.l = n
        self.stream = defaultdict(list)
        self.ptr = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey].append(value)

        if not self.stream[self.ptr]:
            return []
        else:
            ans = []
            while self.stream[self.ptr] and self.ptr <= self.l:
                ans.append(*self.stream[self.ptr])
                self.ptr += 1
            return ans
        



        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)