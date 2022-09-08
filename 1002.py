import sys

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    if abs(r1 - r2) < (x1 - x2) ** 2 + (y1 - y2) ** 2 < r1 + r2:
        print(0)
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 == r1 + r2 \
            or abs(r1 - r2) == (x1 - x2) ** 2 + (y1 - y2) ** 2:
        print(1)
    elif (x1 - x2) ** 2 + (y1 - y2) ** 2 > r1 + r2:
        print(2)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
