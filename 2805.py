n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
while start <= end:
    get_wood = 0
    mid = (start + end) // 2
    for i in trees:
        get_wood += max(0, i - mid)
    # print(f"start: {start}, end: {end}, mid: {mid}, get wood: {get_wood}")
    if get_wood >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)
