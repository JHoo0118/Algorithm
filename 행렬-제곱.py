import sys
import copy
input = sys.stdin.readline


def binary_digit(n):
    result, i = 0, 1
    while n > 0:
        n, r = divmod(n, 2)
        result += r * i
        i *= 10

    return result


def matrix_multiplication(matrix1, matrix2):
    ret = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j] += matrix1[i][k] * matrix2[k][j]
                ret[i][j] %= 1000
    return ret


n, b = map(int, input().split())
a, ret = [], []

for _ in range(n):
    a.append(list(map(int, input().split())))

binary = list(str(binary_digit(b)))
answer = copy.deepcopy(a)
for i in range(1, len(binary)):
    if binary[i] == "0":
        answer = matrix_multiplication(answer, answer)

    elif binary[i] == "1":
        answer = matrix_multiplication(answer, answer)
        answer = matrix_multiplication(answer, a)

for i in range(n):
    for j in range(n):
        answer[i][j] %= 1000

for a in answer:
    print(*a)
