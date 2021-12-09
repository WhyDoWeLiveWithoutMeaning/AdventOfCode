import math

data = open("y21\\Day5\\input.txt", "r").read().splitlines()


class Line:

    straight: bool

    def __init__(self, coord1, coord2, straight=False):
        self.beginning = coord1
        self.end = coord2
        self.straight = straight

    def __repr__(self):
        return f"Line({self.beginning}, {self.end})"

    @property
    def length(self) -> int:
        return math.sqrt(((self.end[0] - self.beginning[0]) ** 2) + ((self.end[1] - self.beginning[1]) ** 2))

    def isStraight(self) -> bool:
        return self.straight


def preProcess(data: list[str]) -> list[Line]:
    lines: list[Line] = []
    for coordinate in data:
        coord1, coord2 = coordinate.split(" -> ")
        x1, y1 = coord1.split(",")
        x2, y2 = coord2.split(",")
        isStraight = False
        if int(x1) == int(x2) or int(y1) == int(y2):
            isStraight = True
        currentLine = Line((int(x1), int(y1)), (int(x2), int(y2)), isStraight)
        lines.append(currentLine)
    return lines


def problem1(lines: list[Line]) -> int:
    """
    This function takes a list of lines and returns how many times at least two lines overlap
    """
    # STEP 1: Create grid.
    grid = getGrid(lines)
    # STEP 2: Mark lines on grid.
    for line in lines:
        if line.isStraight():
            if line.beginning[0] == line.end[0]:
                for y in range(min(line.beginning[1], line.end[1]), max(line.beginning[1], line.end[1])+1):
                    grid[y][line.beginning[0]] += 1
            elif line.beginning[1] == line.end[1]:
                for x in range(min(line.beginning[0], line.end[0]), max(line.beginning[0], line.end[0])+1):
                    grid[line.beginning[1]][x] += 1
    # STEP 3: Count overlaps.
    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] > 1:
                count += 1
    return count

def printArray(a):
    for row in range(len(a)):
        for col in range(len(a[row])):
            print("{}".format(a[row][col]), end=" ")
        print()

def getGrid(lines):
    smallestx = 100
    largestx = 0
    for i in lines:
        if i.beginning[0] < smallestx:
            smallestx = i.beginning[0]
        elif i.end[0] < smallestx:
            smallestx = i.end[0]
        if i.beginning[0] > largestx:
            largestx = i.beginning[0]
        elif i.end[0] > largestx:
            largestx = i.end[0]
    smallesty = 100
    largesty = 0
    for i in lines:
        if i.beginning[1] < smallesty:
            smallesty = i.beginning[1]
        elif i.end[1] < smallesty:
            smallesty = i.end[1]
        if i.beginning[1] > largesty:
            largesty = i.beginning[1]
        elif i.end[1] > largesty:
            largesty = i.end[1]
    grid = []
    for i in range(0, largesty + 1):
        grid.append([])
        for j in range(0, largestx + 1):
            grid[i].append(0)
    return grid

print(problem1(preProcess(data)))
