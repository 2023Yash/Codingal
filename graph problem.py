def numIslands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    visited = set()

    def dfs(r, c):
        if (r, c) in visited or r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return
        visited.add((r, c))
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                islands += 1
                dfs(r, c)
    return islands

grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

count1 = numIslands(grid1)
print(f"Number of islands in grid1 : {count1}")