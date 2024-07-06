class Solution:
    def balancedString(self, s: str) -> int:

        def helper(te , of):
            for i in "QWER":
                if of[i] < te[i]:
                    return False
            return True

        temp = {i : (0-(len(s)//4)) for i in "QWER"}
        offs = {i : 0 for i in "QWER"}
        for i in s:
            temp[i] += 1
        
        for i in temp.keys():
           if temp[i] < 0:
               temp[i] = 0
        
        l = 0
        r = 0
        win = len(s)
        if helper(temp , offs):
            return 0
        while r < len(s):
            offs[s[r]] += 1

            while helper(temp , offs) and l <= r:
                win = min(win , r - l + 1)
                offs[s[l]] -= 1
                l += 1

            
            r += 1
        return win
 



        