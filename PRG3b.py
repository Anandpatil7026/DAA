import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances

def find_optimal_route(graph, start, destination):
    distances = dijkstra(graph, start)
    if distances[destination] == float('inf'):
        return None
    route = []
    node = destination

    while node != start:
        route.append(node)
        neighbors = graph[node]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in neighbors.items():
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                min_distance = distances[neighbor]
                next_node = neighbor
        if next_node is None or next_node in route:
            return None
        node = next_node

    route.append(start)
    route.reverse()
    return route

def get_graph_from_user():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        node = input(f"Enter node {i+1}: ")
        graph[node] = {}
        num_neighbors = int(input(f"Enter the number of neighbors for node {node}: "))
        for j in range(num_neighbors):
            neighbor, weight = input(f"Enter neighbor {j+1} and its weight for node {node} (separated by space): ").split()
            graph[node][neighbor] = int(weight)
    return graph

start_location = input("Enter the start location: ")
destination_location = input("Enter the destination location: ")
graph = get_graph_from_user()

optimal_route = find_optimal_route(graph, start_location, destination_location)

if optimal_route is None:
    print("No valid route exists from the start to the destination.")
else:
    print("Optimal Route:", ' -> '.join(optimal_route))
