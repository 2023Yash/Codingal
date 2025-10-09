def maze_game(moves, directions):
    n = len(moves)
    visited = set()
    pos = 0
    
    while True:
        if pos < 0 or pos >= n:
            return "Out of maze"
        if pos in visited:
            return "Infinite loop"
        
        visited.add(pos)
        if directions[pos] == '>':
            pos += moves[pos]
        else:
            pos -= moves[pos]

print(maze_game([3, 2, 1, 2, 2]))
print(maze_game([1, 1, 1, 1],))
