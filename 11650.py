import sys

N = int(sys.stdin.readline())
xy_list = []
for _ in range(N):
    xy = list(map(int, sys.stdin.readline().split()))
    xy_list.append(xy)
xy_list.sort()
for i in xy_list:
    print(i[0], i[1])
