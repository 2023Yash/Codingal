class Graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_edge = [[] for i in range(self.vertices)]

    def edge(self, u, v):
        self.adj_edge[u].append(v)

    def display(self):
        for i in range(self.vertices):
            print(i, self.adj_edge[i])

g = Graph(5)

g.edge(0, 1)
g.edge(0, 2)
g.edge(1, 2)
g.edge(2, 3)
g.edge(3, 4)

g.display()

class adjacente:
    def __init__(self, data):
        self.data = data
        self.next = None

class adj_graph():
    def __init__(self, vertices):
        self.adj_vertices = vertices
        self.graph = [None] * self.adj_vertices

    def Add_edge(self, src, destination):
        node = adjacente(destination)
        node.next = self.graph[src]
        self.graph[src] = node
        node = adjacente(src)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def display(self):
        for i in range(self.adj_vertices):
            print(i, end=" ")
            temp = self.graph[i]
            while temp:
                print("-->", temp.data, end=" ")
                temp = temp.next
            print()

print()
g2 = adj_graph(5)
g2.Add_edge(0,1)
g2.Add_edge(0, 2)
g2.Add_edge(1, 2)
g2.Add_edge(2, 3)
g2.Add_edge(3, 4)
g2.display()