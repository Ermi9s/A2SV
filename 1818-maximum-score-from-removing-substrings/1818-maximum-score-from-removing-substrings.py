class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def ba_cut(points , st):
            nonlocal y
            stk = []
            tot = 0
            for i in range(len(st)):
                if stk and stk[-1] == "b" and st[i] == "a":
                    stk.pop()
                    points += y
                else:
                    stk.append(st[i])
            
            return [stk ,points]
            
        def ab_cut(points , st):
            nonlocal x
            stk = []
            tot = 0
            for i in range(len(st)):
                if stk and stk[-1] == "a" and st[i] == "b":
                    stk.pop()
                    points += x
                else:
                    stk.append(st[i])
            
            return [stk , points]

        if x >= y:
            new_st,curr_point = ab_cut(0 , s)
            final_st , final_point = ba_cut(curr_point , new_st)
        else:
            new_st,curr_point = ba_cut(0 , s)
            final_st , final_point = ab_cut(curr_point , new_st)
        
        return final_point
