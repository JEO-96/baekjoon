n = int(input())
a = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_result = float("inf")
max_result = float("-inf")


def dfs(index, result):
    global add, sub, mul, div
    if index == n:
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    else:
        if add:
            add -= 1
            dfs(index + 1, result + a[index])
            add += 1
        if sub:
            sub -= 1
            dfs(index + 1, result - a[index])
            sub += 1
        if mul:
            mul -= 1
            dfs(index + 1, result * a[index])
            mul += 1
        if div:
            div -= 1
            dfs(index + 1, int(result / a[index]))
            div += 1


dfs(1, a[0])
print(max_result)
print(min_result)