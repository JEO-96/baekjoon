import sys

S = sys.stdin.readline().rstrip()

D = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        D.add(S[i: j + 1])

print(len(D))