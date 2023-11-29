class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []
        ans = []
        ans.append(num//3) 
        ans.append(num//3)
        ans.append(num//3 + num%3)

        ans[0] -= 1
        ans[2] += 1

        return ans






        