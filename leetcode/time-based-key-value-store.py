class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)
    
    def search(self , time , lst):
        l = 0
        r = len(lst)

        while l+1 < r:
            mid = (l+r)//2

            if lst[mid][1] <= time:
                l = mid
            else:
                r = mid
        
        return "" if not lst  or lst[l][1] > time else lst[l][0]  
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value , timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        return self.search(timestamp , self.store[key])

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)