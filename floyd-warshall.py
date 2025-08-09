cities =['A', 'B', 'C', 'D']
graph = [[0,5,99999,10],
    [99999,0,3,99999],
    [99999,99999,0,1],
    [99999,99999,99999,0]
    ]

def floyd_warshall(graph):
    length = len(graph)
    row_v = [i[:] for i in graph]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                if row_v[j][i] + row_v[i][k] < row_v[j][k]:
                    row_v[j][k] = row_v[j][i] + row_v[i][k]
    return row_v

a = floyd_warshall(graph)

print(" ", end=" ")
for city in cities:
    print(f"{city: <7}", end=" ")
print()
for i in range(len(cities)):
    print(f"{cities[i]:<5}", end = " ")
    for j in range(len(cities)):
        val = a[i][j]
        print(f"{val:<7}", end = " ")
    print()