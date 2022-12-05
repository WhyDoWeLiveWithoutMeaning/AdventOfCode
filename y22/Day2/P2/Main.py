data = open("y22\\Day2\\input.txt", "r").read().splitlines()
total = 0

for battle in data:
    p = battle[0]
    m = battle[2]

    if m == "X":
        if p == "A":
            total += 3
        elif p == "B":
            total += 1
        else:
            total += 2
    elif m == "Y":
        total += 3
        if p == "A":
            total += 1
        elif p == "B":
            total += 2
        else:
            total += 3
    else:
        total += 6
        if p == "A":
            total += 2
        elif p == "B":
            total += 3
        else:
            total += 1



print(total)