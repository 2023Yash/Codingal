def count_trees(graph):
    visited = set()
    tree_count = 0

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if not dfs(neighbor, node):
                    return False
            elif neighbor !=parent:
                return False
        return True

    for node in graph:
        if node  not in visited:
            if dfs(node, -1):
                tree_count+= 1

    return tree_count

graph = {
    0: [1],
    1: [0],
    2: [],
    3: [4],
    4: [3, 5],
    5: [4]
}

print( count_trees(graph))
