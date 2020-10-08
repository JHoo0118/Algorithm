# https://www.acmicpc.net/problem/2589
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]


def bfs(sr, sc):
    queue = deque([(sr, sc, 0)])
    seen = [[0] * m for _ in range(n)]
    seen[sr][sc] = 1
    while queue:
        r, c, cnt = queue.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                continue
            if not seen[nr][nc] and board[nr][nc] == "L":
                seen[nr][nc] = 1
                queue.append((nr, nc, cnt + 1))
    return cnt


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            answer = max(answer, bfs(i, j))
print(answer)
