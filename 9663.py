n = int(input())
row = [0] * n
result = 0


def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    if x == n:
        global result
        result += 1
        return
    for i in range(n):
        row[x] = i
        if check(x):
            dfs(x + 1)


dfs(0)
print(result)
