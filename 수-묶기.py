# https://www.acmicpc.net/problem/1744

def calc(length, arr_type):
    global answer
    if length % 2 == 0:
        i = 0
        while i < length - 1:
            if arr_type[i] == 1 or arr_type[i + 1] == 1:
                answer += arr_type[i] + arr_type[i + 1]
            else:
                answer += arr_type[i] * arr_type[i + 1]
            i += 2
    else:
        i = 0
        while i < length - 2:
            if arr_type[i] == 1 or arr_type[i + 1] == 1:
                answer += arr_type[i] + arr_type[i + 1]
            else:
                answer += arr_type[i] * arr_type[i + 1]
            i += 2
        answer += arr_type[i]


n = int(input())
plus, minus = [], []
for _ in range(n):
    data = int(input())
    if data > 0:
        plus.append(data)
    else:
        minus.append(data)

plus.sort(reverse=True)
minus.sort()
len_plus, len_minus = len(plus), len(minus)
answer = 0

if len_plus > 0:
    calc(len_plus, plus)
if len_minus > 0:
    calc(len_minus, minus)
print(answer)
