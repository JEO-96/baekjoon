A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())
C1, C2 = map(int, input().split())

if A1 == B1:
    X = C1
elif A1 == C1:
    X = B1
elif B1 == C1:
    X = A1

if A2 == B2:
    Y = C2
elif A2 == C2:
    Y = B2
elif B2 == C2:
    Y = A2
print(X, Y)