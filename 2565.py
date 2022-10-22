n = int(input())
a = []
b = []
dp = [1] * n
for i in range(n):
    a.append(list(map(int, input().split())))
a.sort()
for i in range(n):
    b.append(a[i][1])
for i in range(n):
    for j in range(i):
        if b[j] < b[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
