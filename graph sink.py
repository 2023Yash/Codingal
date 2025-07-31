def count_sink_nodes(graph):
    sink_count = 0
    for node in graph:
        if len(graph[node]) == 0:
            sink_count += 1
    return sink_count

graph = {
    0: [1, 2],
    1: [2],
    2: [],
    3: [],
}

print(count_sink_nodes(graph))