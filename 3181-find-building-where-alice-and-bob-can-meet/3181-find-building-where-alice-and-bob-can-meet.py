class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def search(num , stk):
            l = 0
            r = len(stk)

            while l+1 < r:
                mid = (l+r)//2

                if stk[mid][0] > num:
                    l = mid
                else:
                    r = mid

            if not stk:
                return -1
            return stk[l][1] if stk[l][0] > num else -1
    
        for i in range(len(queries)):
            if queries[i][0] > queries[i][1]:
                queries[i][0],queries[i][1] = queries[i][1],queries[i][0]
            queries[i].append(i)
        
        queries.sort(reverse = True , key = lambda x:x[1])
        stk = []

        n = len(heights)
        m = len(queries)
        for i in range(n-1 , queries[0][1] , -1):
            while stk and stk[-1][0] <= heights[i]:
                stk.pop()
            
            stk.append((heights[i] , i))

        ans = [-1 for _ in range(m)]

        
        if heights[queries[0][0]] < heights[queries[0][1]] or queries[0][1] == queries[0][0]:
            ans[queries[0][2]] = queries[0][1]
        else:
            ans[queries[0][2]] = search(heights[queries[0][0]] , stk)
            
   
        l = 0
        def stk_app(left , right):
            for i in range(right , left , -1):
                while stk and stk[-1][0] <= heights[i]:
                    stk.pop()
                stk.append((heights[i] , i))

        # print(queries)
        for r in range(1 , m):
            # print(stk)
            if queries[r][1] != queries[l][1]:
                stk_app(queries[r][1] , queries[l][1])
        
            if heights[queries[r][0]] < heights[queries[r][1]] or queries[r][0] == queries[r][1]:
                ans[queries[r][2]] = queries[r][1]
            else:
                ans[queries[r][2]] = search(heights[queries[r][0]] , stk)
                # print(r , "s" , queries[r])
            # print(".....")
            l += 1
        return ans










                