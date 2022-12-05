data = open("y22\\Day5\\input.txt", "r").read().splitlines()
amount = 0
for line in data:
    if line[1].isdigit():
        amount = int(line[len(line)-2])
        break
arr = [[] for i in range(amount)]
#Gotta Love Coppying the same code
for line in data:
    if line[1].isdigit():
        break
    for i, j in zip(range(1, amount*4, 4), range(amount)):
        if line[i].strip():
            print(line[i], j)
            arr[j].insert(0, line[i])
for line in data:
    if line.startswith("move"):
        u1, amountofcrates, u2, stack1, u3, stack2 = line.split(" ")
        amountofcrates = int(amountofcrates)
        stack1 = int(stack1)
        stack2 = int(stack2)
        whattomove = arr[stack1-1][amountofcrates*-1:]
        arr[stack1-1] = arr[stack1-1][:amountofcrates*-1]
        arr[stack2-1] = arr[stack2-1] + whattomove[::-1] #For P2 Remove [::-1]
finalstr = ""
for i in arr:
    finalstr += i[len(i)-1]
print(finalstr)