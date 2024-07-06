class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """

        suspect = set(range(left,right+1))
        temp = list(suspect)
        for i in temp:
            for r in ranges:
                if i in set(range(r[0] , r[1]+1)):
                    suspect.discard(i)
        
        if not suspect:
            return True
        else:
            return False
