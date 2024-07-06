class UndergroundSystem(object):

    def __init__(self):
        self.history = defaultdict(list)
        self.time = defaultdict(list)
        
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.history[id].append(stationName)
        self.history[id].append(t)
         
    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        places = (self.history[id][0] , stationName)
        
        self.time[places].append(float(t - self.history[id][1]))
        self.history.pop(id)

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return sum(self.time[(startStation,endStation)])/len(self.time[(startStation,endStation)])
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)