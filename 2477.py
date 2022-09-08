K = int(input())
max_width = 0
max_height = 0
max_width_index = 0
max_height_index = 0
arr = []

for i in range(6):
    temp = list(map(int, input().split()))
    arr.append(temp)
    if temp[0] == 1 or temp[0] == 2:
        if max_width < temp[1]:
            max_width = temp[1]
            max_width_index = i
    elif temp[0] == 3 or temp[0] == 4:
        if max_height < temp[1]:
            max_height = temp[1]
            max_height_index = i

subW = abs(arr[(max_width_index - 1) % 6][1] - arr[(max_width_index + 1) % 6][1])
subH = abs(arr[(max_height_index - 1) % 6][1] - arr[(max_height_index + 1) % 6][1])
area = arr[max_width_index][1] * arr[max_height_index][1]
result = (area - subW * subH)
print(result * K)