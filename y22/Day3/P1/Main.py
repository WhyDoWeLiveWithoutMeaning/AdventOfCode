data = open("y22\\Day3\\input.txt", "r").read().splitlines()

def getPoint(letter):
    value = ord(letter)

    if value >= 97:
        return (value - 96)
    elif value >= 65:
        return (value - 38)

def splitString(strin):
    n = len(strin)
    if n%2 == 0:
        return (strin[0:n//2], strin[n//2:])
    else:
        return (strin[0:n//2+1], strin[n//2+1:])

total = 0

for i in data:
    matching_letter = None

    first, second = splitString(i)
    for j in range(len(first)):
        if first[j] in second:
            matching_letter = first[j]
            break

    print(matching_letter, end=" ")
    total += getPoint(matching_letter)
    

print(total)
    