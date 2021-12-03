data = open("y21\\Day3\\input.txt", "r").read().splitlines()


gamma = ""
epsilon = ""
for i in range(0, len(data[0])):
    zero = 0
    one = 0
    for j in data:
        if j[i] == "0":
            zero+=1
        else:
            one+=1
    if zero > one:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

