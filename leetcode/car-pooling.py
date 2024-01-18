class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start = trips[0][1]
        finish = trips[0][2]

        for t in trips:
            if t[1] < start:
                start = t[1]
            if t[2] > finish:
                finish = t[2]
        
        dis = [0] *(finish - start + 2)

        for t in trips:
            dis[t[1]-start] += t[0]
            dis[t[2]-start] -= t[0]
       
        sums = 0
        for i in range(len(dis)):
            sums += dis[i]

            if sums > capacity:
                return False
        return True
        
        
        