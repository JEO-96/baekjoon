import math

merge_count = 0

memo = {
    1: 0,
    2: 2,
    3: 5
}


def merge_sort_count(n, ms_memo):
    if n in ms_memo:
        return ms_memo[n]
    nth_memo = merge_sort_count(math.ceil(n / 2), ms_memo) + merge_sort_count(n - math.ceil(n / 2), ms_memo) + n
    memo[n] = nth_memo
    return nth_memo


def merge_sort(array):
    if len(array) <= 1:
        return list(array)
    else:
        mid = math.ceil(len(array) / 2)
        left = merge_sort(array[:mid])
        right = merge_sort(array[mid:])
        return merge(left, right)


def merge(left_arr: list, right_arr: list):
    l = 0
    r = 0
    result = []
    global merge_count
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] <= right_arr[r]:
            result.append(left_arr[l])
            l += 1
        else:
            result.append(right_arr[r])
            r += 1
        merge_count += 1
        if K == merge_count:
            print(result[-1])
            quit()
    while l >= len(left_arr) and r < len(right_arr):
        result.append(right_arr[r])
        r += 1
        merge_count += 1
        if K == merge_count:
            print(result[-1])
            quit()
    while l < len(left_arr) and r >= len(right_arr):
        result.append(left_arr[l])
        l += 1
        merge_count += 1
        if K == merge_count:
            print(result[-1])
            quit()
    if len(result) == N and K < merge_count:
        print(-1)
        quit()
    return result


N, K = map(int, input().split())
A = list(map(int, input().split()))

if merge_sort_count(N, memo) < K:
    print(-1)
    quit()

merge_sort(A)

