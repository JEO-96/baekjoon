import sys

n = int(sys.stdin.readline())
h = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(1, len(h)):
    h[i][0] += min(h[i - 1][1], h[i - 1][2])
    h[i][1] += min(h[i - 1][0], h[i - 1][2])
    h[i][2] += min(h[i - 1][0], h[i - 1][1])
print(min(h[n - 1][0], h[n - 1][1], h[n - 1][2]))
