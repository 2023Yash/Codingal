def beliman_ford(graph, vertices, source):
    max = 10 ** 9
    distance = [max]*vertices
    distance[source] = 0
    for i in range(vertices - 1):
        for u, v, w in graph:
            if distance[u] != max and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
    for u, v, w in graph:
        if distance[u] != max and distance[u] + w < distance[v]:
            print("Negative no.")
            return None
    return distance

graph = [
    (0,1,6),
    (0,2,7),
    (1,2,8),
    (1,3,5),
    (1,4,-4),
    (2,3,-3),
    (2,4,9),
    (3,1,-2),
    (4,0,2),
    (4,3,7)
]

vertices = 5
source = 0
distance = beliman_ford(graph, vertices, source)

if distance:
    for i in range(vertices):
        print(i, distance[i])