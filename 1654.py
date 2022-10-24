k, n = map(int, input().split())
lan_lines = []
for _ in range(k):
    lan_lines.append(int(input()))
start = 1
end = max(lan_lines)
while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in lan_lines:
        count += i // mid
    # print(f'start: {start}, end: {end}, mid: {mid}, count: {count}')
    if count < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)
