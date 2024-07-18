class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        si,sj=-1,-1
        x=2
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    si,sj=i,j
                elif grid[i][j]==0:
                    x+=1
        directions=((0,1),(0,-1),(1,0),(-1,0))
        dq=deque()
        dq.append(((si,sj),{(si,sj)}))
        ans=0
        while dq:
            arr,seen=dq.popleft()
            i,j=arr
            if grid[i][j]==2:
                if len(seen)==x: ans+=1
                continue
            for di,dj in directions:
                ni,nj=i+di,j+dj
                if 0<=ni<m and 0<=nj<n and grid[ni][nj]!=-1 and (ni,nj) not in seen:
                    seen.add((ni,nj))
                    dq.append(((ni,nj),seen.copy()))
                    seen.remove((ni,nj))
        return ans
                
