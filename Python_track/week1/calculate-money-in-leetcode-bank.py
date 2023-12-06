class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """

        mondays = n // 7
        left_days = n%7
        start = 1
        end = 8
        sums = 0
        if n <= 7:
            return sum(range(1,n+1))

        for _ in range(mondays):
            sums += sum(range(start,end))
            start += 1
            end += 1
        
        for _ in range(left_days):
            sums += start
            start += 1
        
        return sums

        