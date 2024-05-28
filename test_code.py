p = [7, 1, 5, 3, 6, 4]
profit = 0
for x, y in zip(p, p[1:]):
    profit += max(y - x, 0)

print(profit)
