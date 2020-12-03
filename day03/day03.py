f = open('day03Input.txt', 'r').read()

array = f.split('\n')

lengthHorizontal = len(array[0])

x = 0
count = 0

for yIdx in range(0, len(array)):
    if array[yIdx][x] == '#':
        count += 1
    x = (x + 3) % lengthHorizontal

print(count)