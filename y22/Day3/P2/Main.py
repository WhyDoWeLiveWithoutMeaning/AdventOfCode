import numpy

ionpLine = open("y22\\Day3\\input.txt", "r").read().splitlines()

data = [list(i) for i in
    list(
        numpy.array_split(
            numpy.array(
                ionpLine
            ),len(ionpLine)/3
        )
    )
]

def getPoint(letter):
    value = ord(letter)

    if value >= 97:
        return (value - 96)
    elif value >= 65:
        return (value - 38)

total = 0
for i in data:
    matching_letter = None

    first, second, third = tuple(i)
    for j in range(len(first)):
        if first[j] in second and first[j] in third:
            matching_letter = first[j]
            break

    print(matching_letter, end=" ")
    total += getPoint(matching_letter)
    

print(total)
    