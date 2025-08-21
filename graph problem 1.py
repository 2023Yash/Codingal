def is_safe(graph, color, node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring_util(graph, m, color, node):
    if node == len(graph):
        return True

    for c in range(1, m+1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring_util(graph, m, color, node+1):
                return True
            color[node] = 0
    return False

def graph_coloring(graph, m):
    color = [0] * len(graph)
    # Call utility function here instead of itself
    if graph_coloring_util(graph, m, color, 0):
        return True
    return False
