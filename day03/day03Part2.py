f = open('day03Input.txt', 'r').read()

array = f.split('\n')

lengthHorizontal = len(array[0])


def getNumberOfTrees(dx, dy):
    x = 0
    count = 0

    for yIdx in range(0, len(array), dy):
        if array[yIdx][x] == '#':
            count += 1
        x = (x + dx) % lengthHorizontal
    return count


accessArray = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

val = 1

for i in accessArray:
    val = val * getNumberOfTrees(i[0], i[1])

print(val)
