import sys

Y = 0
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    Y += a * b

if Y == X:
    print("Yes")
else:
    print("No")