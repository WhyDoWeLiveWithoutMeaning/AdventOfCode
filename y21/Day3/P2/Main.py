import copy
data = open("y21\\Day3\\input.txt", "r").read().splitlines()

poop = copy.deepcopy(data)


def findoxy(data):
    for i in range(0, len(data[0])):
        if len(data) == 1:
            print(data)
            return data
        zer = 0
        one = 0
        for j in data:
            if j[i] == "0":
                zer += 1
            else:
                one += 1
        if zer > one:
            data = list(filter(lambda x : x[i] == "0", data))
        else:
            data = list(filter(lambda x : x[i] == "1", data))
    return data

def findc02(data):
    for i in range(0, len(data[0])):
        if len(data) == 1:
            print(data)
            return data
        zer = 0
        one = 0
        for j in data:
            if j[i] == "0":
                zer += 1
            else:
                one += 1
        if zer > one:
            data = list(filter(lambda x : x[i] == "1", data))
        else:
            data = list(filter(lambda x : x[i] == "0", data))
    return data

        


print(int(findoxy(data)[0],2) * int(findc02(data)[0],2))

