class Bitset(object):

    def __init__(self, size):
        """
        :type size: int
        """
        self.Bitset = [ 0 for i in range(size)]
        self.flipo = [ 1 for i in range(size)]
        self.counto = 0
        self.countz = size
        self.size = size

    def fix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if idx < self.size and self.Bitset[idx] == 0:
            self.Bitset[idx] = 1
            self.flipo[idx] = 0
            self.counto += 1
            self.countz -= 1

    
    def unfix(self, idx):
        """
        :type idx: int
        :rtype: None
        """
        if idx < self.size and self.Bitset[idx] == 1:
            self.Bitset[idx] = 0
            self.flipo[idx] = 1
            self.counto -= 1
            self.countz += 1
        
    def flip(self):
        """
        :rtype: None
        """
        temp = self.flipo
        self.flipo = self.Bitset
        self.Bitset = temp

        tempo = self.counto
        self.counto = self.countz
        self.countz = tempo
        
    def all(self):
        """
        :rtype: bool
        """
        return self.counto == self.size
   
    def one(self):
        """
        :rtype: bool
        """
        return self.counto
        
    def count(self):
        """
        :rtype: int
        """
        return self.counto
        
    def toString(self):
        """
        :rtype: str
        """
        t = [str(i) for i in self.Bitset]
        return "".join(t)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()