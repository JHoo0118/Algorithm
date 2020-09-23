import sys
from collections import deque
m, n, h = map(int, input().split())
board = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
# https://www.acmicpc.net/problem/7569

dz = [0, 0, 0, 0, 1, -1]
seen = [[[0] * m for _ in range(n)] for _ in range(h)]


def bfs():
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if board[i][j][k] == 1:
                    queue.append((i, j, k, 0))
                    seen[i][j][k] = 1

    while queue:
        z, r, c, cnt = queue.popleft()
        for i in range(6):
            nz = z + dz[i]
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or nz < 0 or nz >= h:
                continue

            if board[nz][nr][nc] == 0 and seen[nz][nr][nc] == 0:
                seen[nz][nr][nc] = 1
                board[nz][nr][nc] = 1
                queue.append((nz, nr, nc, cnt + 1))
    return cnt


result = bfs()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if board[i][j][k] == 0:
                print(-1)
                sys.exit(0)
print(result)
