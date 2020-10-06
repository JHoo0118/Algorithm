# https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())
info = []
for _ in range(n):
    info.append(list(map(int, input().split())))
dp = [0] * (k + 1)
for i in range(n):
    new_dp = dp[:]
    w, v = info[i]
    for j in range(k):
        jw = j + w
        if jw <= k:
            new_dp[jw] = max(new_dp[jw], dp[j] + v)
    dp = new_dp
print(dp[-1])
