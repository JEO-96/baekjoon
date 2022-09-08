import sys
import collections

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
dic = collections.Counter(N_list)

for i in M_list:
    if i in dic:
        print(dic[i], end=' ')
    else:
        print(0, end=' ')