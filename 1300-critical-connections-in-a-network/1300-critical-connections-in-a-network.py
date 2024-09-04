class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for a,b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs():
            stk = [(0 , 0 , -1)]
            seen = [0 for _ in  range(n)]

            disc = {}
            low = {}

            time = 0

            ans = []

            while stk:
                
                node,state,par = stk.pop()

                if state:
                    for nbr in graph[node]:
                        if nbr != par and disc[node] < low[nbr]:
                            ans.append([node , nbr])
                
                        if nbr != par:
                            low[node] = min(low[node] , low[nbr])
                            # print(node , "nbr" , nbr  , low[nbr], "par" , par)
                        # print(node , low[node])
                    continue
                
                if seen[node]:
                    continue

                disc[node] = time
                low[node] = time
                time += 1

                seen[node] = 1
                stk.append((node , 1 , par))
                for nbr in graph[node]:
                    if not seen[nbr]:
                        stk.append((nbr , 0 , node))
            
            # print(low)
            return ans
        


        return dfs()






        