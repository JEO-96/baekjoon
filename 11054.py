n = int(input())
dp1 = [0] * n
arr = list(map(int, input().split()))

for i in range(n):
    tmp = 0
    length = 0
    for j in range(n):
        if j < i:
            if tmp < arr[j] < arr[i]:
                tmp = arr[j]
                length += 1
        elif j > i:
            if arr[i] > tmp
