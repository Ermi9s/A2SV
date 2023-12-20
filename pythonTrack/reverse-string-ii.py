class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        def flipper(arr):
            reverse = []
            while arr:
                reverse.append(arr.pop())
            
            return reverse 
        
        lst = [i for i in s] 

        for i in range(0,len(s),2*k):
            lst[i:i+k] = flipper(lst[i:i+k])

        return "".join(lst)

        