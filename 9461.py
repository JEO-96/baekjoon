import sys

t = int(sys.stdin.readline())
p = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    result = p[-1] + p[-5]
    p.append(result)
for _ in range(t):
    n = int(sys.stdin.readline())
    print(p[n])
