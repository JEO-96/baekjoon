graph = [list(map(int, input().split())) for i in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            blank.append((i, j))


def check_row(x, val):
    for i in range(9):
        if val == graph[x][i]:
            return False
    return True


def check_col(y, val):
    for i in range(9):
        if val == graph[i][y]:
            return False
    return True


def check_rect(x, y, val):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if val == graph[nx + i][ny + j]:
                return False
    return True


def dfs(depth):
    if depth == len(blank):
        for i in range(9):
            print(*graph[i])
        exit()

    for i in range(1, 10):
        x = blank[depth][0]
        y = blank[depth][1]
        if check_row(x, i) and check_col(y, i) and check_rect(x, y, i):
            graph[x][y] = i
            dfs(depth + 1)
            graph[x][y] = 0


dfs(0)
