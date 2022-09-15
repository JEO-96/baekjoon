import sys
import collections

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    names = []
    result = 1
    for i in range(n):
        A, B = sys.stdin.readline().split()
        names.append(B)
    num = collections.Counter(names)
    for key in num:
        result *= num[key] + 1
    print(result - 1)
