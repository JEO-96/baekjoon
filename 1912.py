input()
l = list(map(int, input().split()))
_sum = [l[0]]
for i in range(len(l) - 1):
    _sum.append(max(_sum[i] + l[i + 1], l[i + 1]))
print(max(_sum))
