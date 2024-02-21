class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float('-inf')
        shot = 0
        points.sort(key = lambda x:x[1])
        print(points)

        for b in points:
            if end < b[0]: 
                end = b[1]
                shot += 1
        
        return shot


        