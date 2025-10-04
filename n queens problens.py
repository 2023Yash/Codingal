def solve_n_queens(n):
    board = [-1] * n
    solutions = []
    def is_safe(row,col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True

    def place_queen(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n ):
            if is_safe(row, col):
                board[row] =  col
                place_queen(row + 1)
                board[row]= -1

    place_queen(0)
    return solutions

result = solve_n_queens(8)
print(len(result))
