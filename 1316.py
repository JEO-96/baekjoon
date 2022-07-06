N = int(input())
count = 0
for i in range(N):
    word = input()
    is_group = True
    for j in range(len(word) - 1):
        if word[j] != word[j + 1]:
            if word[j] in word[j+1:]:
                is_group = False
                break
    if is_group:
        count += 1
print(count)