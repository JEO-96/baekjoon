n, c = map(int, input().split())
houses = []
for _ in range(n):
    houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]

result = 0

while start <= end:
    mid = (start + end) // 2
    count = 1
    current = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]
    # print(f"start: {start}, end: {end}, count: {count}, c: {c} mid: {mid}")
    if count < c:
        end = mid - 1
    else:
        start = mid + 1
print(end)