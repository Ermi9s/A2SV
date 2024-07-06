class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        can = capacity

        for i in range(len(plants)):
            if plants[i] <= can:
                can -= plants[i]
                steps += 1
            else:
                steps += (2*i + 1)
                can = capacity - plants[i]
        
        return steps




        # if i have enough watter and subtract and step ++  
        #if i dont give wy u have and add the index to step and fill
        #
        #
        #
        