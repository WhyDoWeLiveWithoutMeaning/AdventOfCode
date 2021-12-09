data = [n1 for n1 in open("y21\\Day8\\input.txt").read().splitlines()]
splitData = []
for z in data:
    splitData.append(tuple(z.split("|")))
i8 = 0
i7 = 0
i4 = 0
i1 = 0
for _, d in splitData:
    signals = d.strip().split(" ")
    for signal in signals:
        if len(signal) == 7:
            i8+=1
        elif len(signal) == 4:
            i4+=1
        elif len(signal) == 3:
            i7+=1
        elif len(signal) == 2:
            i1+=1
print("Instance of 8:", i8)
print("Instance of 7:", i7)
print("Instance of 4:", i4)
print("Instance of 1:", i1)
print(i8 + i7 + i4 + i1)