import sys

N, M = map(int, sys.stdin.readline().split())
count = 0
dic = {}
for i in range(N):
    _str = sys.stdin.readline().rstrip()
    dic[_str] = i

for i in range(M):
    _str = sys.stdin.readline().rstrip()
    if _str in dic:
        count += 1

print(count)