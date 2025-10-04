from collections import defaultdict

def add_edge(graph, u, v):
    graph[u].append(v)

def count_paths_util(graph, u, dest, visited):
    visited[u] = True

    if u == dest:
        visited[u] = False
        return 1

    count = 0
    for neighbor in graph[u]:
        if not visited[neighbor]:
            count +=  count_paths_util(graph, neighbor, dest, visited)
    visited[u] = False
    return count

def count_paths(graph, src, dest, V):
    visited = [False] * V
    return count_paths_util(graph, src, dest, visited)

V = 5
graph = defaultdict(list)

add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 0, 3)
add_edge(graph, 2, 0)
add_edge(graph, 2, 1)
add_edge(graph, 1, 3)

src = 2
dest = 3

print("Total number of paths:", count_paths(graph, src, dest, V))
