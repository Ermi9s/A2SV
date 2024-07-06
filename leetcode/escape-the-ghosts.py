class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        g_dis = float('inf')
        for i in ghosts:
            g_dis = min((abs(target[0] - i[0]) + abs(target[1] - i[1])),g_dis)
        
       
        if g_dis > abs(target[0])+abs(target[1]):
            return True
        else:
            return False


        