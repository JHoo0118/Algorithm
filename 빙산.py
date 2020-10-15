# https://www.acmicpc.net/problem/2573

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(r, c):
    queue = deque([(r, c)])
    val[r][c] == 1
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if val[nr][nc] == 0 and arr[nr][nc] != 0:
                queue.append((nr, nc))
                val[nr][nc] = 1


while True:
    val = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] != 0:
                cnt = 0
                for dr, dc in directions:
                    nr, nc = i + dr, j + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= m:
                        continue
                    if arr[nr][nc] == 0:
                        cnt += 1
                val[i][j] = cnt
    for i in range(n):
        for j in range(m):
            arr[i][j] = max(0, arr[i][j] - val[i][j])
    ans += 1
    cnt = 0
    val = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if val[i][j] == 0 and arr[i][j] != 0:
                bfs(i, j)
                cnt += 1
    if cnt >= 2:
        print(ans)
        break

    elif cnt == 0:
        print(0)
        break
