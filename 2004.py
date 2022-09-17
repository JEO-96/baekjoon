def count_num(N, K):
    count = 0
    while N != 0:
        N //= K
        count += N
    return count


n, m = map(int, input().split())
print(min(count_num(n, 2) - count_num(n - m, 2) - count_num(m, 2),
          count_num(n, 5) - count_num(n - m, 5) - count_num(m, 5)))
