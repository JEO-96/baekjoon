import sys

N, M = map(int, sys.stdin.readline().split())
illustrated_book = {}
for i in range(1, N + 1):
    a = sys.stdin.readline().rstrip()
    illustrated_book[a] = i
    illustrated_book[i] = a

for i in range(M):
    x = sys.stdin.readline().rstrip()
    if x.isdigit():
        x = int(x)
    print(illustrated_book[x])
