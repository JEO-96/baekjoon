n = int(input())

dp = [0] * n
glass = []
for i in range(n):
    glass.append(int(input()))
dp[0] = glass[0]
if n > 1:
    dp[1] = dp[0] + glass[1]
if n > 2:
    dp[2] = max(dp[0] + glass[2], glass[1] + glass[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i - 1], dp[i - 3] + glass[i - 1] + glass[i], dp[i - 2] + glass[i])
print(max(dp))