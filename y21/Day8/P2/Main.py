data = [n1 for n1 in open("y21\\Day8\\input.txt").read().splitlines()]

splitData = []

for z in data:
    splitData.append(tuple(z.split("|")))

total = 0

def s1Ins2(s1, s2):
    for i in s1:
        if i not in s2:
            return False
    return True

for s, d in splitData:
    signals = s.strip().split(" ")
    knowAllValues = False
    vals = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
        7: "",
        8: "",
        9: ""
    }
    for signal in signals:
        if len(signal) == 7:
            vals[8] = signal
        elif len(signal) == 4:
            vals[4] = signal
        elif len(signal) == 3:
            vals[7] = signal
        elif len(signal) == 2:
            vals[1] = signal
    while not knowAllValues:
        for signal in signals:
            if signal not in vals.values():
                if len(signal) == 6:
                    if s1Ins2(vals[4], signal) and vals[9] == "":
                        vals[9] = signal
                    elif s1Ins2(vals[7], signal) and vals[0] == "":
                        vals[0] = signal
                    elif vals[6] == "":
                        vals[6] = signal
                elif len(signal) == 5:
                    if vals[6] != "":
                        if s1Ins2(vals[7], signal) and vals[3] == "":
                            vals[3] = signal
                        elif s1Ins2(signal, vals[6]) and vals[5] == "":
                            vals[5] = signal
                        elif vals[2] == "":
                            vals[2] = signal
        for v in range(len(vals)):
            if vals[v] == "":
                knowAllValues = False
                break
            else:
                knowAllValues = True
    number = ""
    for c in d.strip().split(" "):
        for k, v in zip(vals.keys(), vals.values()):
            if s1Ins2(c, v) and len(c) == len(v):
                number += str(k)
    total+=int(number)
print(total)