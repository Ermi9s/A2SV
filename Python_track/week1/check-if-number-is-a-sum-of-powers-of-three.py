class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n:
            rem = n % 3
            n = n // 3
            if rem == 2:
                return False
        return True

        