class Solution(object):
    def distanceBetweenBusStops(self, dis, s, d):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """

        if s <= d:
            min_dis = min(sum(dis[s:d]) , (sum(dis[:s]) + sum(dis[d:])))
        else:
            min_dis = min(sum(dis[d:s]) , (sum(dis[:d]) + sum(dis[s:])))           


        return min_dis
        
        # [7,10,1,12,11,14,5,0]
        # 7  > 2

        # between the s and d or outwars
        # [s:d]
        # [:s] + [d:]


        