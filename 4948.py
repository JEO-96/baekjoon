num = []
for i in range(2, 123456 * 2 + 1):
    check = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            check = False
            break
    if check:
        num.append(i)

while True:
    N = int(input())
    if N == 0:
        break
    count = 0
    for i in num:
        if N < i <= 2 * N:
            count += 1
    print(count)