A, B = map(int, input().split())
C = int(input())
B = B + C
while B >= 60:
    B -= 60
    A += 1
    while A >= 24:
        A -= 24
print(A, B)