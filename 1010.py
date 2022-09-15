import sys


def factorial(num: int):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


T = int(sys.stdin.readline())
for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(factorial(M) // (factorial(N) * factorial(M - N)))
