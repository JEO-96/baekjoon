import sys

n = int(sys.stdin.readline())
s = []
dp = []
for _ in range(n):
    s.append(int(sys.stdin.readline()))

dp.append(s[0])
if n > 1:
    dp.append(max(s[1], s[0] + s[1]))
if n > 2:
    dp.append(max(s[0] + s[2], s[1] + s[2]))
for i in range(3, n):
    dp.append(max(dp[i - 2] + s[i], dp[i - 3] + s[i - 1] + s[i]))
print(dp[-1])