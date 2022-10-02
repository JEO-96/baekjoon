import math

n = int(input())
m = []
num_list = [int(input()) for _ in range(n)]
num_list.sort()
diff_num_list = []
for i in range(len(num_list)- 1):
    diff_num_list.append(num_list[i + 1] - num_list[i])

gcd = diff_num_list[0]

for i in range(1, len(diff_num_list)):
    gcd = math.gcd(gcd, diff_num_list[i])

for i in range(2, int(math.sqrt(gcd)) + 1):
    if gcd % i == 0:
        m.append(i)
        m.append(gcd // i)

m = list(set(m))
m.append(gcd)
m.sort()
print(*m)