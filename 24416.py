count1 = 0
count2 = 0
f = {}


def fib(n):
    global count1
    count1 += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fibonacci(n):
    global count2

    f[1], f[2] = 1, 1
    for i in range(3, n + 1):
        if i not in f:
            count2 += 1
            f[i] = f[i - 1] + f[i - 2]
    return f[n]


N = int(input())
c1 = fibonacci(N)
print(c1, count2)
