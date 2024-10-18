def find_paths(n, m, i=0, j=0, path='', paths=[]):
    if i == n - 1 and j == m - 1:
        paths.append(path)
        return

    if j < m - 1:
        find_paths(n, m, i, j + 1, path + 'R', paths)

    if i < n - 1:
        find_paths(n, m, i + 1, j, path + 'D', paths)

    return paths

n, m = 3, 3
all_paths = find_paths(n, m)
print(all_paths)
