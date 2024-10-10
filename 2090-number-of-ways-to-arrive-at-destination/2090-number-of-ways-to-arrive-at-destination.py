class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b,w in roads:
            graph[a].append((b , w))
            graph[b].append((a , w))
        
        ways = [0]*n
        ways[0] = 1
        dis = [float('inf')]*n
        dis[0] = 0
        heap = [(0 , 0)]
        pro = [0]*n

        while heap:
            d,node = heappop(heap)

            if pro[node]:
                continue
            
            pro[node] = 1

            for nbr,w in graph[node]:
                update = d+w
                if update < dis[nbr]:
                    dis[nbr] = update
                    ways[nbr] = ways[node]%(int(1e9 + 7))
                    heappush(heap , (update , nbr))
                elif update == dis[nbr]:
                    ways[nbr] += ways[node]%(int(1e9 + 7))
        

        return ways[n-1]%(int(1e9 + 7))





        