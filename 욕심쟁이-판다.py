# https://www.acmicpc.net/problem/1937

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
survive = [[0] * n for _ in range(n)]


def check(r, c):
    if survive[r][c]:
        return survive[r][c]
    survive[r][c] = 1
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if arr[r][c] < arr[nr][nc]:
            survive[r][c] = max(survive[r][c], check(nr, nc) + 1)
    return survive[r][c]


answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, check(i, j))
print(answer)
