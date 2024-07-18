class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edges_with_indices = [(a, b, c, i) for i, (a, b, c) in enumerate(edges)]
        edges_with_indices.sort(key=lambda x: x[2])
        max_cost = 1000 * 100

        def calculate_mst_cost(edge_set, node_set, current_cost):
            if len(node_set) == n:
                return current_cost
            else:
                for a, b, c, i in edges_with_indices:
                    if i not in edge_set and ((a in node_set and b not in node_set) or (a not in node_set and b in node_set)):
                        return calculate_mst_cost(edge_set | set([i]), node_set | set([a, b]), current_cost + c)
            return max_cost
        
        initial_mst_cost = calculate_mst_cost(set(), set([0]), 0)

        critical, pseudo_critical = [], []
        for a, b, c, i in edges_with_indices:
            if calculate_mst_cost(set([i]), set([0]), 0) > initial_mst_cost:
                critical.append(i)
            elif calculate_mst_cost(set([i]), set([a, b]), c) == initial_mst_cost:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]