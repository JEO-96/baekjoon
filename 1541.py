formula = input()
split_minus = formula.split("-")

result = sum(map(int, split_minus[0].split("+")))
for i in range(1, len(split_minus)):
    result -= sum(map(int, split_minus[i].split("+")))

print(result)
