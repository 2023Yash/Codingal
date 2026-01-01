def find_valid_paths(maze):
    n = len(maze)
    m = len(maze[0])
    all_paths = []
    def backtrack(i, j, current_path, has_neg1):
        if i >= n or j >= m:
            return
        current_path.append((i, j))
        if maze[i][j] == -1:
            has_neg1 = True
        if i == n - 1 and j == m - 1:
            if has_neg1:
                all_paths.append(list(current_path))
                current_path.pop()
        return
    backtrack(i + 1, j, current_path, has_neg1)
    backtrack(i, j + 1, current_path, has_neg1)
    current_path.pop()
    backtrack(0, 0, [], False)
    return all_paths
maze = [[0, 0, -1], [0, -1, 0], [0, 0, 0]]
paths = find_valid_paths(maze)
for p in paths:
    print(p)