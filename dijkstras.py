def is_safe(graph, vertex, color, c):
    for i in range(len(graph)):
        if graph[vertex][i] == 1 and color[i] == c:
            return False
    return True


def graph_coloring_util(graph, m, color, vertex):
    if vertex == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, vertex, color, c):
            color[vertex] = c
            if graph_coloring_util(graph, m, color, vertex + 1):
                return True
            color[vertex] = 0

    return False


def graph_coloring(graph, m):
    n = len(graph)
    color = [0] * n
    if graph_coloring_util(graph, m, color, 0):
        print("Solution exists: Coloring =", color)
        return True
    else:
        print("No solution exists with", m, "colors")
        return False