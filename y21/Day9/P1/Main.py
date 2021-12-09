input = open("y21\\Day9\\input.txt").read().splitlines()

data = []
for line in input:
    data.append([int(i) for i in line])

def cns(arr, x1, y1, x2, y2) -> bool:
    try:
        if x2 < 0 or y2 < 0:
            raise IndexError
        if arr[x1][y1] < arr[x2][y2]:
            return True
        else:
            return False
    except:
        return True


def get_lowspot_index(arr: list[list[int]]) -> list[(int,int)]:
    lowspot = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if cns(arr, i, j, i-1, j) and cns(arr, i, j, i+1, j) and cns(arr, i, j, i, j-1) and cns(arr, i, j, i, j+1):
                lowspot += 1 + data[i][j]
    return lowspot

print(get_lowspot_index(data))