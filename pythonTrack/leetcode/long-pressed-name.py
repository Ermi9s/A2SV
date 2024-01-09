class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0
        r = 0
        prev = name[0]
     
        while r < len(typed) and l < len(name):
            while r < len(typed) and typed[r] == prev and typed[r] != name[l]:
                r += 1

            if l < len(name) and r < len(typed) and typed[r] == name[l]:
                prev = name[l]
                l += 1
                r += 1
                
            else:
                return False


        while r < len(typed):
            if typed[r] != name[-1]:
                return False
            r += 1
        while l < len(name):
            if typed[-1] != name[l]:
                return False
            l += 1
        return True

        


        

        