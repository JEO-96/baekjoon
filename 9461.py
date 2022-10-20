import sys

t = int(sys.stdin.readline())
for _ in range(t):
    p = [0, 1, 1, 1, 2, 2]
    n = int(sys.stdin.readline())
    if n <= 5:
        print(p[n])
    else:
        for i in range(6, n + 1):
            result = p[-1] + p[-5]
            p.append(result)
        print(p[-1])
