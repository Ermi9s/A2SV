class Solution:
    def decodeString(self, s: str) -> str: 
        def decode(l , r):
            ans = ""
            op = 0 
            start = -1
            db = ""
            m = 1
            for i in range(l , r):
                if s[i].isdigit():
                    db += s[i]
                elif s[i] == '[':          
                    if op == 0:
                        start = i
                        m = int(db)
                    op += 1
                    db = ""
                elif s[i] == ']':
                    op -= 1
                    if op == 0:
                        ans += m * decode(start+1 , i)
                elif op == 0:
                    ans += s[i]
            
            return ans
                

               
        return decode(0 , len(s))



    