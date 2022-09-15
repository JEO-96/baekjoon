N = int(input())
num = 1
count = 0
for i in range(2, N + 1):
    num *= i

while num % 10 == 0:
    count += 1
    num = num // 10

print(count)