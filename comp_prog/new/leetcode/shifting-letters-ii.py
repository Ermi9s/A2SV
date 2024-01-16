class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        t_shifts = [0]*(len(s) + 1)

        for i in shifts:
            if i[2] == 0:
                t_shifts[i[0]] -= 1
                t_shifts[i[1] + 1] += 1
            else:
                t_shifts[i[0]] += 1
                t_shifts[i[1] + 1] -= 1

        for i in range(1 ,len(t_shifts)):
            t_shifts[i] += t_shifts[i - 1]
        
        ch = {(i + 96):chr(ord('a') + i - 1) for i in range(1 , 27)}
        
        ans = []
        for i in range(len(s)):
            ind = (((ord(s[i]) - 97) + t_shifts[i]) % 26) + 97
            ans.append(ch[ind])


       
        return "".join(ans)


        



        





        