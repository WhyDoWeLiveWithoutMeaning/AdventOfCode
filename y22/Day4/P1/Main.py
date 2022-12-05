data = open("y22\\Day4\\input.txt", "r").read().splitlines()

t = 0

def isAinB(A, B):
    for i in A:
        if i not in B:
            return False
    return True

for line in data:

    first, second = line.split(",")

    firstRange = list(range(int(first.split("-")[0]), int(first.split("-")[1])+1))
    secondRange = list(range(int(second.split("-")[0]), int(second.split("-")[1])+1))

    if isAinB(firstRange, secondRange) or isAinB(secondRange, firstRange):
        t += 1

print(t) 
