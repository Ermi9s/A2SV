class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for a,b,c in edges:
            graph[a].append((b, c))
            graph[b].append((a , c))
        
        def dj(src):
            dis = [float('inf')]*n
            dis[src] = 0
            pro = [False]*n
            heap = [(0 , src)]

            while heap:
                d,node = heappop(heap)
                
                if pro[node]:
                    continue
                pro[node] = True

                for nbr,w in graph[node]:
                    update = d+w
                    if dis[nbr] > update:
                        dis[nbr] = update
                        heappush(heap , (update , nbr))
            
            return dis
        
        ans = [-1]*n
        for node in range(n-1 , -1 , -1):
            dis = dj(node)
            for d in dis:
                if d <= distanceThreshold:
                    if ans[node] == -1:
                        ans[node]+=1
                    ans[node] += 1
        
        mini = float('inf')

        for i in range(len(ans)):
            if ans[i] != -1:
                mini = min(mini , ans[i])
        
        for i in range(n-1 , -1 , -1):
            if ans[i] == mini:
                return i
                    
        

        