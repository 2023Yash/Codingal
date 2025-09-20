def suduko_board(board):
    row = [set() for i in range(9)]
    col = [set() for i in range(9)]
    boxes = [set() for i in range(9)]

    for i in range(9):
        for j in range(9):
            num = board[i][j]
            if num != 0:
                row[i].add(num)
                col[j].add(num)
                boxes[(i//3)*3+(j//3)].add(num)

    def backtraking(r, c):
        if r==9:
            return True
        if c==9:
            return backtraking(r + 1, 0)
        if board[r][c] != 0:
            return backtraking(r, c + 1)
        
        for i in range(1, 10):
            index = (r // 3) * 3 +(c // 3)
            if i not in row[r] and i not in col[c] and i not in boxes[index]:
                board[r][c] = i
                row[r].add(i)
                col[c].add(i)
                boxes[index].add(i)
                if backtraking(r, c+1):
                    return True

                board[r][c] = 0
                row[r].remove(i)
                col[c].remove(i)
                boxes[index].remove(i)
        return False
    return backtraking(0, 0)

def printboard(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end = " ")
        print()

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
if suduko_board(board):
    print("solved!")
    printboard(board)
else:
    print("Something is wrong")