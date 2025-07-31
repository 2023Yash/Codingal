def dijktras_algorthm(graph, start):
    node = list(graph.keys())
    distance = {}
    for i in node:
        distance[i] = 9999999

    distance[start] = 0
    visited = []
    while len(visited) < len(node):
        min_node = None
        min_distance = 9999999

        for j in node:
            if j not in visited and distance[j] < min_distance:
                min_distance = distance[j]
                min_node = j
        if min_node is None:
            break
        
        for neighbour, weight in graph[min_node]:
            if neighbour not in visited:
                new_distance = distance[min_node] + weight
                if new_distance < distance[neighbour]:
                    distance[neighbour] = new_distance
        visited.append(min_node)
    return distance

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("C", 2), ("D", 5)],
    "C": [("A", 4), ("B", 2), ("D", 1)],
    "D": [("B", 5), ("C", 1)]
}

start = "A"
u = dijktras_algorthm(graph, start)

for i in u:
    print(start, "to", i, "=", u[i])