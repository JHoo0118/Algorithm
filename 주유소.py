# https://www.acmicpc.net/problem/13305

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

calc = [0] * (n - 1)
calc[0] = price[0] * road[0]
min_price = price[0]
for i in range(1, n - 1):
    if price[i] < min_price:
        min_price = price[i]
    calc[i] = calc[i - 1] + min_price * road[i]
print(calc[-1])
