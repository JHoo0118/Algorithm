import copy
INF = 1e9
n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board.append([0] * m)
answer = 0


def set_archer(count):
    global answer
    if count == 3:
        field = copy.deepcopy(board)
        result = bfs(field)
        answer = max(answer, result)
        return
    for j in range(m):
        if board[n][j] == 0:
            board[n][j] = 2
            set_archer(count + 1)
            board[n][j] = 0


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(field):
    result = 0
    archer_pos = []
    for j in range(m):
        if field[n][j] == 2:
            archer_pos.append((n, j))

    for _ in range(n):
        enemy_pos = []
        dist = [INF] * 3
        for k in range(3):
            r, c = 0, 0
            for i in range(n - 1, -1, -1):
                for j in range(m):
                    if field[i][j] == 1:
                        distance = abs(
                            archer_pos[k][0] - i) + abs(archer_pos[k][1] - j)
                        if distance <= d:
                            if dist[k] > distance:
                                dist[k] = distance
                                r, c = i, j

                            elif dist[k] == distance:
                                if c > j:
                                    r, c = i, j

            if dist[k] != INF:
                if (r, c) not in enemy_pos:
                    enemy_pos.append((r, c))

        if len(enemy_pos) > 0:
            for row, col in enemy_pos:
                field[row][col] = 0
                result += 1

        for j in range(m):
            for i in range(n - 1, 0, -1):
                field[i][j] = field[i - 1][j]
        for j in range(m):
            field[0][j] = 0

    return result


set_archer(0)
print(answer)
