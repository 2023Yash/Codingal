class Graph:
    def __init__(self):
        self.graph = {}

    def add_edges(self, u, v):
        self.graph.setdefault(u, []).append(v)
        self.graph.setdefault(v, []).append(u)

    def display(self):
        for key in self.graph:
            print(self.graph[key])
    
g = Graph()
g.add_edges(0, 1)
g.add_edges(1, 2)
g.add_edges(3, 4)
g.add_edges(5, 6)
g.add_edges(7, 8)
g.display()

class Graph_Matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for i in range(vertices)]

    def add_edge(self, u ,v):
        self.graph[u][v]=1
        self.graph[v][u]=1

    def display(self):
        for i in self.graph:
            print(i)

gra = Graph_Matrix(5)
gra.add_edge(0, 1)
gra.add_edge(1, 2)
gra.add_edge(2, 3)
gra.add_edge(3, 4)
gra.display()