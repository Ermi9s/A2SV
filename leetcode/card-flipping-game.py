class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        flag = { i: True for i in fronts}
        
        minGood = float('inf')
        good = float('inf')
        for i in backs:
            if i not in set(fronts):
                good = i
            minGood = min(good , minGood)
        
        for f,b in zip(fronts,backs):
            if f == b:
                flag[f] = False

        for f,b in zip(fronts,backs):
            if f!=b and flag[f]:
                minGood = min(f , minGood)
        
        return minGood if minGood != float('inf') else 0


            
                
            
