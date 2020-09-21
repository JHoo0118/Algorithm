# https://www.acmicpc.net/problem/14503
n, m = map(int, input().split())
current_row, current_col, heading = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


def turn_left():
    global heading
    heading -= 1
    if heading == -1:
        heading = 3


while True:
    if board[current_row][current_col] == 0:
        board[current_row][current_col] = 2
    if board[current_row + 1][current_col] != 0 and board[current_row - 1][current_col] != 0 and board[current_row][current_col + 1] != 0 and board[current_row][current_col - 1] != 0:
        if heading == 0 or heading == 2:
            if heading == 0:
                i = 1
            elif heading == 2:
                i = -1
            if board[current_row + i][current_col] == 1:
                break
            current_row += i

        elif heading == 1 or heading == 3:
            if heading == 1:
                i = -1
            elif heading == 3:
                i = 1
            if board[current_row][current_col + i] == 1:
                break
            current_col += i
        continue

    i = 0
    if heading == 0 or heading == 2:
        if heading == 0:
            i = -1
        elif heading == 2:
            i = 1
        if board[current_row][current_col + i] == 0:
            current_col += i
        turn_left()
        continue

    if heading == 1 or heading == 3:
        if heading == 1:
            i = -1
        elif heading == 3:
            i = 1
        if board[current_row + i][current_col] == 0:
            current_row += i
        turn_left()
        continue

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            answer += 1
print(answer)
