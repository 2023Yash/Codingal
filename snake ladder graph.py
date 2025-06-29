from collections import deque

def min_dice_throws(board, N):
    visited = [False] * N
    queue = deque()

    queue.append((0, 0))
    visited[0] = True

    while queue:
        position, moves = queue.popleft()

        if position == N - 1:
            return moves

        for dice in range(1, 7):
            next_pos = position + dice
            if next_pos < N and not visited[next_pos]:
                visited[next_pos] = True
                final_pos = board[next_pos] if board[next_pos] != -1 else next_pos
                queue.append((final_pos, moves + 1))

    return -1

N = 100
board = [-1] * N
board[2] = 21
board[4] = 7
board[10] = 25
board[19] = 28
board[26] = 55
board[70] = 90