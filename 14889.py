import sys

n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
team1 = []

min_score = float("inf")


def dfs(index: int):
    if index == n // 2:
        team2 = []
        global min_score
        score1 = 0
        score2 = 0
        for i in range(n):
            if i not in team1:
                team2.append(i)
        for i in range(n // 2 - 1):
            for j in range(i + 1, n // 2):
                score1 += s[team1[i]][team1[j]] + s[team1[j]][team1[i]]
                score2 += s[team2[i]][team2[j]] + s[team2[j]][team2[i]]
        min_score = min(min_score, abs(score1 - score2))
        return
    for i in range(n):
        if len(team1) > 0 and i < team1[len(team1) - 1]:
            continue
        if i not in team1:
            team1.append(i)
            dfs(index + 1)
            team1.pop()


dfs(0)
print(min_score)
