class RandomizedSet(object):

    def __init__(self):
        self.ind = {}
        self.arr = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.ind: return False
        self.arr.append(val)
        self.ind[val] = len(self.arr)-1
        return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.ind:
             return False
             
        temp = self.ind[val]
        self.ind[self.arr[-1]] = temp
        self.arr[temp] = self.arr[-1]
        self.ind.pop(val)
        self.arr.pop()
        
        return True
    
    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()