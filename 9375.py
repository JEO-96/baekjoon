import sys
import collections


T = int(sys.stdin.readline())
for _ in range(T):
    wearing = collections.defaultdict(int)
    n = int(sys.stdin.readline())
    names = []
    result = 1
    for i in range(n):
        A, B = sys.stdin.readline().split()
        if B not in names:
            names.append(B)
        wearing[B] += 1
    for j in names:
        result *= wearing[j] + 1
    print(result - 1)