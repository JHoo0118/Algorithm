# https://www.acmicpc.net/problem/13547

import sys
input = sys.stdin.readline
n = int(input())
size = int(n**.5)
a = [0]+list(map(int, input().split()))
m = int(input())
query = [tuple(map(int, input().split())) + (idx,) for idx in range(m)]
query.sort(key=lambda x: (x[0] // size * size, x[1]))
count = [0] * (max(a) + 1)
answer = [0] * m
current = left = right = 0
for i, j, idx in query:
    if right == 0:
        for k in range(i, j + 1):
            if count[a[k]] == 0:
                current += 1
            count[a[k]] += 1
        left, right = i, j
        answer[idx] = current
        continue
    while left < i:
        count[a[left]] -= 1
        if count[a[left]] == 0:
            current -= 1
        left += 1
    while i < left:
        left -= 1
        if count[a[left]] == 0:
            current += 1
        count[a[left]] += 1
    while right < j:
        right += 1
        if count[a[right]] == 0:
            current += 1
        count[a[right]] += 1
    while j < right:
        count[a[right]] -= 1
        if count[a[right]] == 0:
            current -= 1
        right -= 1
    answer[idx] = current
print(*answer, sep='\n')
