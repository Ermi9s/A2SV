class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        temp = []
        pre = []

        for i in range(len(s)):
            if s[i] == "|":
                temp.append(i)

            if not pre and s[i]=="*":
                pre.append(1)
            elif not pre and s[i]=="|":
                pre.append(0)
            elif pre and s[i]=="*":
                pre.append(pre[-1] + 1) 
            elif pre and s[i]=="|":
                pre.append(pre[-1])

        if not temp:
            return [0]
        def searchLeft(num):
            l = -1
            r = len(temp)-1

            while l + 1 < r:
                mid = (l+r)//2

                if temp[mid] < num:
                    l = mid
                else:
                    r = mid

            return temp[r]

        def searchRight(num):
            l = 0
            r = len(temp)

            while l+1 < r:
                mid = (l+r)//2

                if temp[mid] > num:
                    r = mid
                else:
                    l = mid
            
            return temp[l]
        
        ans = []

        for qr in queries:
            left = searchLeft(qr[0])
            right = searchRight(qr[1])

            ans.append(pre[right] - pre[left]) if pre[right] - pre[left] > 0 else ans.append(0) 
        
        return ans

        