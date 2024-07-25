class Solution(object):
    def isPalindrome(self, x):
        y = str(x) 
        j = 0

        for i in range(len(y)-1,0,-1):
            if y[i] !=  y[j]:
                return False
            j += 1
        
        return True

        