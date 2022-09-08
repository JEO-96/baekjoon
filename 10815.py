import sys

N = int(sys.stdin.readline())
NL = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
ML = list(map(int, sys.stdin.readline().split()))
NL.sort()


def binary_search(num):
    l = 0
    r = N - 1

    while l <= r:
        mid = (l + r) // 2
        if NL[mid] == num:
            return 1
        elif NL[mid] > num:
            r = mid - 1
        else:
            l = mid + 1

    return 0


for num in ML:
    print(binary_search(num), end=' ')
