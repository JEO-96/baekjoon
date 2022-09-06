import sys

cnt = 0
W, H, X, Y, P = map(int, input().split())


def is_in_rectangle(x, y):
    if X <= x <= X + W and Y <= y <= Y + H:
        return True
    else:
        return False


def is_in_circle(x, y):
    radius = H / 2
    if ((X - x) ** 2 + (Y + radius - y) ** 2) ** (1 / 2) <= radius \
            or ((X + W - x) ** 2 + (Y + radius - y) ** 2) ** (1 / 2) <= radius:
        return True
    else:
        return False


for i in range(P):
    x, y = map(int, sys.stdin.readline().split())
    if is_in_rectangle(x, y) or is_in_circle(x, y):
        cnt += 1

print(cnt)