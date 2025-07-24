def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)

def dfs(u, graph, visited):
    visited[u] = True
    for i in graph[u]:
        if not visited[i]:
            dfs(i, graph, visited)

def treeCount(graph, V):
    visited = [False] * V
    count = 0
    for i in range(V):
        if not visited[i]:
            dfs(i, graph, visited)
            count += 1
    return count
    
V = 7
graph = [[] for i in range(V)]
addEdge(graph, 0, 1)
addEdge(graph, 1, 2)
addEdge(graph, 3, 4)
addEdge(graph, 5, 6)
print(treeCount(graph, V))

def minRabbits(answer, N):
    Map = {}
    for i in range(N):
        if answer[i] in Map:
            Map[answer[i]] += 1
        else:
            Map[answer[i]] = 1

    count = 0
    for i in Map:
        x = i
        y = Map[i]

        if y%(x+1) == 0:
            count = count + (y // (x + 1)) * (x +1)
        else:
            count = count + ((y // (x + 1)) + 1) * (x +1)

    return count

arr = [2, 2, 0]
N = len(arr)
print(minRabbits(arr, N))