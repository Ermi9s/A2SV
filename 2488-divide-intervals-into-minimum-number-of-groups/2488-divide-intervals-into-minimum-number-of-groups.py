class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        mx = 0

        for _,r in intervals:
            mx = max(mx , r)

        pre = [0]*(mx+2)

        for l,r in intervals:
            pre[l] += 1
            pre[r+1] -= 1
        
        for i in range(1 , len(pre)):
            pre[i] += pre[i-1]
        
        return max(pre)
