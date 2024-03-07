class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = -1
        r = len(arr)

        ch = {arr[i]:abs(x-arr[i]) for i in range(len(arr))}

        while l+1 < r:
            mid = (l+r)//2

            if arr[mid] < x:
                l = mid
            else:
                r = mid 
        
        ans = []

        print(l , r)

        while l >= 0 and r < len(arr) and len(ans) < k:
            if ch[arr[l]] < ch[arr[r]]:
                ans.append(arr[l])
                l -= 1
            elif ch[arr[l]] > ch[arr[r]]:
                ans.append(arr[r])
                r += 1
            else:
                ans.append(arr[l])
                l -= 1
            
         

        while l >= 0 and len(ans) < k:
            ans.append(arr[l])
            l -= 1
            
        while r < len(arr) and len(ans) < k:
            ans.append(arr[r])
            r += 1
        

        return sorted(ans)




        
        