def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()

    print(start, end = " ")
    visited.add(start)

    for neighbor in graph [start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["D", "F"],
    "F": ["C", "E"]
}

dfs(graph, "A")

def graph_func(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbhor in graph[node]:
                stack.append(neighbhor)
    return visited
    
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
} 

visited = graph_func(graph, "A")

print(visited)