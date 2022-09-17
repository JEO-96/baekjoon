N, M = map(int, input().split())
s = []


def n_m():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in range(1, N + 1):
        if len(s) < 1 or i >= s[-1]:
            s.append(i)
            n_m()
            s.pop()


n_m()
