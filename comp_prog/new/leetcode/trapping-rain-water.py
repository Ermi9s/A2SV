class Solution:
    def trap(self, height: List[int]) -> int:
        stk = []
        
        ans = 0

        for i in range(len(height)):
            while stk and height[i] >= stk[-1][1]:
                dip = stk.pop()
                if stk:
                    wid = i - stk[-1][0] - 1
                    top = stk[-1][1]
                    ans += ((wid) * (min(top - dip[1] , height[i] - dip[1])))
  
                else:
                    dip = height[i]
                    break
                

            stk.append([i , height[i]])
        
        return ans

        