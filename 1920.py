n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
b = map(int, input().split())


def binary(target: int, arr: list, start: int, end: int) -> int:
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return 1
    elif target < arr[mid]:
        return binary(target, arr, start, mid - 1)
    else:
        return binary(target, arr, mid + 1, end)


for i in b:
    print(binary(i, a, 0, len(a) - 1))
