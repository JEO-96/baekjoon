import sys

n = int(sys.stdin.readline())
meetings = []  # [start, end]

for _ in range(n):
    meetings.append(list(map(int, sys.stdin.readline().split())))
meetings.sort(key= lambda x: (x[1], x[0]))

end_time = meetings[0][1]
count = 1
for i in range(1, n):
    if end_time <= meetings[i][0]:
        count += 1
        end_time = meetings[i][1]
print(count)
