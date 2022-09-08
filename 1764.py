import sys

dic = {}
N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    name = sys.stdin.readline().rstrip()
    dic[name] = i

count = 0
name_list = []
for i in range(M):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        count += 1
        name_list.append(name)

name_list.sort()
print(count)
for i in name_list:
    print(i)