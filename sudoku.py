def princode(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()

def saving_valid_moves(board, row, col, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    for j in range(9):
        if board[j][col] == num:
            return False

    row_start = row - row % 3
    col_start = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[row_start + i][col_start + j] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if saving_valid_moves(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],

    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],

    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

if solve_sudoku(board):
    princode(board)
else:
    print("Invalid game numbers")