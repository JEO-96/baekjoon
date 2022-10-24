import sys

n, k = map(int, sys.stdin.readline().split())
a = []
cnt = 0

for _ in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

for i in reversed(range(n)):
    cnt += k//a[i]
    k = k % a[i]
    # print(f"k:{k}, a[i]:{a[i]}, count:{cnt}")
print(cnt)