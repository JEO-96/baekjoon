N, M = map(int, input().split())
s = []


def n_m():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            n_m()
            s.pop()


n_m()
