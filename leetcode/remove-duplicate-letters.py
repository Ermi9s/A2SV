class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        seen = set()
        ch = Counter(s)

        stk = []

        for i in range(len(s)):
            while stk and ord(stk[-1]) >= ord(s[i]) and ch[stk[-1]] > 1 and (s[i] not in seen):
                temp = stk.pop()
                ch[temp] -= 1
                seen.remove(temp)
    
            if s[i] not in seen:
                stk.append(s[i])
                seen.add(s[i])
            else:
                ch[s[i]] -= 1
        

        return ''.join(stk)





        

        
        


        

        

        


        