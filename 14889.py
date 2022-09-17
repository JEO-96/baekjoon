import sys

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
start_team = []
min_diff = float("inf")


def dfs(index):
    if index == N // 2:
        global min_diff
        start_score = 0
        link_score = 0
        link_team = []
        for i in range(N):
            if i not in start_team:
                link_team.append(i)
        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                start_score += S[start_team[i]][start_team[j]] + S[start_team[j]][start_team[i]]
                link_score += S[link_team[i]][link_team[j]] + S[link_team[j]][link_team[i]]
        min_diff = min(min_diff, abs(start_score - link_score))
        return
    for i in range(N):
        if i not in start_team:
            if len(start_team) > 0 and start_team[-1] > i:
                continue
            start_team.append(i)
            dfs(index + 1)
            start_team.pop()


dfs(0)
print(min_diff)
