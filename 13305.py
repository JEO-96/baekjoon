n = int(input(""))
roads = list(map(int, input("").split()))
prices = list(map(int, input("").split()))

cost = 0
buy_cost = float("inf")
for i in range(n - 1):
    if buy_cost > prices[i]:
        buy_cost = prices[i]
    cost += buy_cost * roads[i]
    # print(f"cost: {cost}")
print(cost)
