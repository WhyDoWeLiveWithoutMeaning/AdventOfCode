data = [int(i) for i in open('y21\\Day6\\input.txt').read().split(',')]
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for d in data:
    arr[d] += 1
    print(arr)
for i in range(256):
    print(arr, i)
    a0 = arr[0]
    arr[0] = arr[1]
    arr[1] = arr[2]
    arr[2] = arr[3]
    arr[3] = arr[4]
    arr[4] = arr[5]
    arr[5] = arr[6]
    arr[6] = arr[7] + a0
    arr[7] = arr[8]
    arr[8] = a0
print(sum(arr))