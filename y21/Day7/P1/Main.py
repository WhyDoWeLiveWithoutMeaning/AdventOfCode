data = [int(i) for i in open('y21\\Day7\\input.txt').read().split(',')]

lowest = min(data)
highest = max(data)

lowestFuel = 1000000000000000

for i in range(lowest, highest + 1):
    fuelCost = 0
    for crab in data:
        fuelCost += max(crab, i) - min(crab, i)
    if fuelCost < lowestFuel:
        lowestFuel = fuelCost
print(lowestFuel)