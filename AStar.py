import heapq

# Define Tamil Nadu cities and distances
graph = {
    'Chennai': {'Vellore': 150, 'Trichy': 330, 'Madurai': 450},
    'Vellore': {'Chennai': 150, 'Salem': 200},
    'Salem': {'Vellore': 200, 'Madurai': 230},
    'Trichy': {'Chennai': 330, 'Madurai': 130},
    'Madurai': {'Trichy': 130, 'Salem': 230, 'Coimbatore': 215},
    'Coimbatore': {'Madurai': 215}
}

# Heuristic (Estimated time in hours assuming 60 km/hr)
heuristic = {
    'Chennai': 8, 'Vellore': 6, 'Salem': 4, 'Trichy': 5, 
    'Madurai': 3, 'Coimbatore': 2
}

def a_star(start, goal):
    queue = []
    heapq.heappush(queue, (0, start, []))
    visited = set()

    while queue:
        cost, city, path = heapq.heappop(queue)

        if city in visited:
            continue
        visited.add(city)

        path = path + [city]
        if city == goal:
            return path, cost

        for neighbor, distance in graph[city].items():
            if neighbor not in visited:
                g_cost = cost + distance
                f_cost = g_cost + heuristic.get(neighbor, 0)
                heapq.heappush(queue, (f_cost, neighbor, path))

    return None

path, distance = a_star('Chennai', 'Coimbatore')
print("Optimal Path:", path, "Total Distance:", distance, "km")
