data = open("y22\\Day1\\input.txt", "r").read().splitlines()

elfs: list = []

t = 0
for i in data:

    if i.strip() != "":
        t += int(i)
    else:
        elfs.append(t)
        t = 0
elfs.sort(reverse=True)
print(elfs[0] + elfs[1] + elfs[2])
        