import sys

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

    if abs(r2 - r1) < d < r1 + r2:
        print(2)
    elif d == 0 and r1 == r2:
        print(-1)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)
    else:
        print(0)
