# https://www.acmicpc.net/problem/14501

n = int(input())
times = []
prices = []
max_value = 0
for i in range(1, n + 1):
    time, price = map(int, input().split())
    times.append(time)
    prices.append(price)
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    if i + times[i] <= n:
        dp[i] = max(max_value, prices[i] + dp[i + times[i]])
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
