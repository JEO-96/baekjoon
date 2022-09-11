import sys

count = 0
T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    for i in range(n):
        cx, cy, r = map(int, sys.stdin.readline().split())
        d1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** (1 / 2)
        d2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** (1 / 2)
        if d1 > r > d2 or d2 > r > d1:
            count += 1
    print(count)
    count = 0
