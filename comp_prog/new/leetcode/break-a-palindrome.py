class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        palindrome = list(palindrome)
        if len(palindrome) == 1:
            return ""
        
        mir = ord('z')
        ind = 0

        for i in range(len(palindrome)):
            if len(palindrome) % 2 and i == len(palindrome)//2:
                continue
            if palindrome[i] == 'a':
                temp = mir
                mir = min(mir , ord('b'))
                if temp < mir:
                    continue
                ind = i

            else:
                temp = mir
                mir = min(mir , ord('a'))
                if temp != mir:
                    ind = i
                break
        print(ind)
        print(mir)
        palindrome[ind] = chr(mir) 

        return "".join(palindrome)
