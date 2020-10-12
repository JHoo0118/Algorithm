# https://www.acmicpc.net/problem/5558
from collections import deque


def bfs(sr, sc, tr, tc):
    queue = deque([(sr, sc, 0)])
    seen = [[0] * w for _ in range(h)]
    seen[sr][sc] = 1
    while queue:
        r, c, cnt = queue.popleft()
        if (r, c) == (tr, tc):
            return cnt
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= h or nc < 0 or nc >= w:
                continue
            if not seen[nr][nc] and a[nr][nc] != "X":
                queue.append((nr, nc, cnt + 1))
                seen[nr][nc] = 1


h, w, n = map(int, input().split())
sr, sc = 0, 0
a, c = [], [0] * 10
ans = 0
for i in range(h):
    row = list(input())
    for j in range(w):
        if row[j] == "S":
            sr, sc = i, j
        elif row[j].isdigit():
            row[j] = int(row[j])
            c[int(row[j])] = [i, j]
    a.append(row)

for coords in c:
    if coords == 0:
        continue
    ans += bfs(sr, sc, coords[0], coords[1])
    sr, sc = coords[0], coords[1]
print(ans)
