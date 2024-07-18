class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if target == source:
            return 0
        
        stops_to_routes = {}

        # Create mapping from stops to routes
        for i, route in enumerate(routes):
            for stop in route:
                if stop not in stops_to_routes:
                    stops_to_routes[stop] = []
                stops_to_routes[stop].append(i)

        if source not in stops_to_routes or target not in stops_to_routes:
            return -1
        q = deque(stops_to_routes[source])
        visited_routes = set()

        num_bus_routes = 1

        while q:
            size = len(q)
            for _ in range(size):
                current_route = q.popleft()
                
                if target in routes[current_route]:
                    return num_bus_routes
                
                for stop in routes[current_route]:
                    for route in stops_to_routes[stop]:
                        if route not in visited_routes:
                            q.append(route)
                            visited_routes.add(route)

            num_bus_routes += 1
        
        return -1
        