from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_paths_util(self, u, d, visited):
        if u == d:
            return 1

        visited[u] = True
        path_count = 0
        for nbr in self.graph[u]:
            if not visited[nbr]:
                path_count += self.count_paths_util(nbr, d, visited)

        visited[u] = False
        return path_count

    def count_paths(self, s, d):
        visited = [False] * self.V
        return self.count_paths_util(s, d, visited)
