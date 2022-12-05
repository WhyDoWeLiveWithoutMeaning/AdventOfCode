data = open("y22\\Day2\\input.txt", "r").read().splitlines()

total = 0

def getPoint(choice:str) -> int:
    if choice == "X":
        return 1
    if choice == "Y":
        return 2
    if choice == "Z":
        return 3
    else:
        return 0

for battle in data:
    p = battle[0]
    m = battle[2]

    if (p == "A" and m == "X") or (p == "B" and m == "Y") or (p == "C" and m == "Z"): # Draw Condition
        total += 3 + getPoint(m)
    elif (p == "A" and m == "Y") or (p == "B" and m == "Z") or (p == "C" and m == "X"): #Win Conidition
        total += 6 + getPoint(m)
    else:
        total += getPoint(m)


print(total)