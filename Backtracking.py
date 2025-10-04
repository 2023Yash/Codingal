def count_islands(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def dfs(r, c):
        visited[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and
                matrix[nr][nc] == 1 and not visited[nr][nc]):
                dfs(nr, nc)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1

    return count

matrix = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [1, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 0, 1]
]

print("Number of islands:", count_islands(matrix))
