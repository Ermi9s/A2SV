class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for a,b in relations:
            graph[a].append(b)
            indegree[b] += 1

        took = [0 for _ in range(n)]

        def topsort():
            que = deque()
            ans = 0

            for node in range(1 , n+1):
                if indegree[node] == 0:
                    que.append(node)

            while que:
                node = que.popleft()
                time_spent = took[node-1] + time[node-1]

                for nbr in graph[node]:
                    took[nbr-1] = max(took[nbr-1] , time_spent)
                    indegree[nbr] -= 1
                    if indegree[nbr] == 0:
                        que.append(nbr)
                        
                ans = max(ans , time_spent)
            
            return ans
        
        return topsort() 
                    

                

            


        