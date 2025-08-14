def n_quenns(n):
    def is_safe(board, row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i, j = row - 1, col - 1
            while i >=0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                j -= 1
                i -= 1

            i, j = row - 1, col + 1

            while i >=0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            return True
    
    def solve(row):
         if row == n:
              result.append(["".join(r) for r in board])
              return
         
         for col in range(n):
              if is_safe(board, row, col):
                   board[row][col] = "Q"
                   solve(row+1)
                   board[row][col] = " . "
                   
    result = []
    board = [[" . " for i in range(n)] for j in range(n)]
    solve(0)
    return result

n = 4
res = n_quenns(n)
print(len(res))
for i, j in enumerate(res, 1):
    print(i)
    for row in j:
         print(row)
    print()