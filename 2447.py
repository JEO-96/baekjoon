def draw_star(N):
    if N == 3:
        return ["***", "* *", "***"]
    arr = draw_star(N // 3)
    stars = []

    for i in arr:
        stars.append(i * 3)
    for i in arr:
        stars.append(i + " " * (N // 3) + i)
    for i in arr:
        stars.append(i * 3)

    return stars


n = int(input())
print("\n".join(draw_star(n)))
