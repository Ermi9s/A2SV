class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """

        k = 3
        candidate = float('-inf')

        for i in range(len(num)-k+1):
            if len(set(num[i:k+i])) == 1:        
                candidate = max(candidate,int(num[i:i+k]))
        
        if candidate == 0:
            return "000" 
        elif candidate == float('-inf'):
            return ""
        else:
            return str(candidate) 

        