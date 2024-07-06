class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        ans = [0,0]

        ans[0] = (celsius + 273.15)
        ans[1] = ((celsius * 1.8) + 32)

        return ans

        