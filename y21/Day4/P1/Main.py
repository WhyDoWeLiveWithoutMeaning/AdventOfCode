data = open("y21\\Day4\\input.txt", "r").read().splitlines()

numbers = [int(n) for n in data[0].split(",")]

bingoCards = []

b = [[],[],[],[],[]]
t = 0
for i in data[1:]:
    # print(i)
    if i.strip() == "":
        bingoCards.append(b)
        b = [[],[],[],[],[]]
        t = 0
    else:
        for e in i.split(" "):
            if e == "":
                continue
            b[t].append(int(e))
        t+=1
    # print(b)
bingoCards.append(b)

bingoCards.pop(0)
# print(bingoCards)

def bingoWin(bingoCard, called):
    # Check Rows
    for i in range(len(bingoCard)):
        nums = 0
        for j in range(len(bingoCard)):
            if bingoCard[i][j] in called:
                nums += 1
        if nums >= 5:
            return True
    
    # Check Cols
    for i in range(len(bingoCard)):
        nums = 0
        for j in range(len(bingoCard)):
            if bingoCard[j][i] in called:
                nums += 1
        if nums >= 5:
            return True
    return False

def winningBingoCard(bingoCards, called):
    for card in bingoCards:
        if bingoWin(card, called):
            return card
    return False

called = []
winningCard = []
for i in numbers:
    called.append(i)
    card = winningBingoCard(bingoCards,called)

    if card:
        winningCard = card
        print(card)
        break
outsid = 0
for i in winningCard:
    for k in i:
        if k not in called:
            outsid += k
print(outsid*called[-1])






