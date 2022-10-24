n = int(input())
p = list(map(int, input().split()))
p.sort()
result = []
_sum = 0
for i in p:
    _sum += i
    result.append(_sum)
print(sum(result))
