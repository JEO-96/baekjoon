import sys

d = {}


def w(a: int, b: int, c: int) -> int:
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif a < b < c:
        if (a, b, c) in d:
            result = d[(a, b, c)]
        else:
            result = d[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return result
    else:
        if (a, b, c) in d:
            result = d[(a, b, c)]
        else:
            result = d[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return result


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')
