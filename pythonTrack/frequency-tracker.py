class FrequencyTracker(object):

    def __init__(self):
        self.frequency = defaultdict(int)
        self.freq = defaultdict(int)
        
    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]:
            self.freq[self.frequency[number]] -= 1
            self.frequency[number] += 1
            self.freq[self.frequency[number]] += 1     
        else:
            self.frequency[number] += 1
            self.freq[self.frequency[number]] += 1
        
    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if self.frequency[number]:
            self.freq[self.frequency[number]] -= 1
            self.frequency[number] -= 1
            self.freq[self.frequency[number]] += 1


    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return self.freq[frequency]
        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)