import sys

count = 0
value = 0


def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


T = int(sys.stdin.readline())

for i in range(T):
    S = sys.stdin.readline().rstrip()
    value = isPalindrome(S)
    print(value, count)
    count = 0
