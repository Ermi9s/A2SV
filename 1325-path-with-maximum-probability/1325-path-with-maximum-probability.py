class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            a,b = edges[i]
            graph[a].append((b , succProb[i]))
            graph[b].append((a , succProb[i]))
        
        probability = [0]*n
        probability[start_node] = 1
        heap = [(-1, start_node)]
        pro = [0]*n

        while heap:
            p,node = heappop(heap)

            if pro[node]:
                continue
            pro[node] = 1

            for nbr,w in graph[node]:
                update = -p*w
                if update > probability[nbr]:
                    probability[nbr] = update
                    heappush(heap , (-update , nbr))
        

        return probability[end_node]

        