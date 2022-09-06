import sys

A_count, B_count = map(int, sys.stdin.readline().split())

A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))
result1 = list(A - B)
result2 = list(B - A)
result = result1 + result2

print(len(result))