class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for a,b,w in times:
            graph[a].append((b , w))

        def dj(source):
            distances = [float('inf')]*(n+1)
            distances[source] = 0
            processed = [0]*(n+1)
            heap = [(0 , source)]

            while heap:
                dis,node = heappop(heap)
                
                if processed[node]:
                    continue
                processed[node] = 1

                for nbr,w in graph[node]:
                    update = dis + w
                    if update < distances[nbr]:
                        distances[nbr] = update
                        heappush(heap , (update , nbr))
            
            return distances
        
        minDis = dj(k)
        ans = float('-inf')

        for node in range(1 , n+1):
            ans = max(ans , minDis[node])
        
        return ans if ans != float('inf') else -1
                


        