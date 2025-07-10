class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = [[] for i in range(v)]

    def addedge(self, v, w):
        self.adj[v].append(w)

    def DFS(self, s):
        visited = [False for i in range(self.v)]

        stack = []
        stack.append(s)

        while(len(stack)):
            s = stack[-1]
            stack.pop()

            if not visited[s]:
                print(s, end=' ')
                visited[s] = True
            
            for node in self.adj[s]:
                if not visited[node]:
                    stack.append(node)

f = Graph(5)
f.addedge(1, 0)
f.addedge(0, 2)
f.addedge(2, 1)
f.addedge(0, 3)
f.addedge(1, 4)

print("this is the traversal:")
f.DFS(0)