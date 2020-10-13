# https://www.acmicpc.net/problem/1939
import sys
from collections import deque
input = sys.stdin.readline
def MI(): return map(int, input().split())


n, m = MI()
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = MI()
    graph[a].append((b, c))
    graph[b].append((a, c))
st, ed = MI()


def bfs(st, ed, v):
    queue = deque([st])
    s = set([st])
    while queue:
        p = queue.popleft()
        if p == ed:
            return True
        for i in graph[p]:
            if i[0] not in s and i[1] >= v:
                s.add(i[0])
                queue.append(i[0])
    return False


start, end = 1, 1_000_000_000
answer = 0
while start <= end:
    mid = (start + end) // 2
    if bfs(st, ed, mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)
