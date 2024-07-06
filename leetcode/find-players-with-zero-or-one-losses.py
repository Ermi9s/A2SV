class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = []
        win = set()
        lose = set()

        losers = {}

        for i in matches:
            losers[i[1]] = losers.get(i[1],0) + 1
        
        key = set(losers.keys())
        for i in matches:
            if i[0] not in key:
                win.add(i[0])

        answer.append(list(win))
        
        for i in matches:
            if losers[i[1]] == 1:
                lose.add(i[1])
        
        answer.append(list(lose))

        answer[0].sort()
        answer[1].sort()
        
        return answer
        

        