class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        maxi = max(candies)
        ans = []

        for i in candies:
            ans.append(i + extraCandies >= maxi)
            
        
        return ans


        