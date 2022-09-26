N, M = map(int, input().split())

num_arr = []


def dfs(index):
    if index == M:
        print(*num_arr)
        return
    for i in range(1, N + 1):
        if i not in num_arr:
            num_arr.append(i)
            dfs(index + 1)
            num_arr.pop()


dfs(0)
