# https://www.acmicpc.net/problem/15686

from itertools import combinations
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

house, chicken = [], []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

chicken_list = list(combinations(chicken, m))
answer = 1e9
for candidate in chicken_list:
    distance_sum = 0
    for hx, hy in house:
        tmp = 1e9
        for cx, cy in candidate:
            tmp = min(tmp, abs(hx - cx) + abs(hy - cy))
        distance_sum += tmp
    answer = min(answer, distance_sum)
print(answer)