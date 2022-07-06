A, B, C = map(int, input().split())
if A == B == C:
    print(10000 + A * 1000)
elif A == B:
    print(1000 + A * 100)
elif A == C:
    print(1000 + A * 100)
elif B == C:
    print(1000 + B * 100)
else:
    num = max(A, B, C)
    print(num * 100)