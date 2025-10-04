def find_paths(maze):
    n = len(maze)
    m = len(maze[0])
    all_paths = []

    def dfs(i, j, path, has_neg):
        if i >= n or j >= m:
            return
        path.append((i, j))
        if maze[i][j] == -1:
            has_neg = True

        if i == n - 1 and j == m - 1:
            if has_neg:
                all_paths.append(path[:])
            path.pop()
            return
        dfs(i, j + 1, path, has_neg)
        dfs(i + 1, j, path, has_neg)
        path.pop()

    dfs(0, 0, [], False)
    return all_paths


maze = [
    [0,  0, -1],
    [0, -1,  0],
    [0,  0,  0]
]

paths = find_paths(maze)
print(len(paths))
for p in paths:
    print(p)
