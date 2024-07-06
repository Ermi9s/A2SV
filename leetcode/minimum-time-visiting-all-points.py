class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        steps = 0

        def find_difference(present,future):
            diference = [0,0]
            for i in range(2):
                diference[i] = abs(future[i] - present[i])
            return diference                  
        
        for f in range(1,len(points)):
            steps += max(find_difference(points[f-1],points[f]))
            
        
        return steps

            


        

        

        