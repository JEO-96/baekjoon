n = int(input())
a = list(map(int, input().split()))
dp1 = [1] * n
dp2 = [1] * n
a_reverse = a[::-1]
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if a_reverse[j] < a_reverse[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
result = [0] * n
for i in range(n):
    result[i] = dp1[i] + dp2[n - i - 1] - 1

print(max(result))
