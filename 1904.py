n = int(input())

np1 = 1
np2 = 2
res = 1 if n == 1 else 2
for i in range(2, n):
    res = (np1 + np2) % 15746
    np1, np2 = np2, res
print(res)
