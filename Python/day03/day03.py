with open('Day03Input.txt', 'r') as f:
    data = f.read()

array = data.split('\n')
len_horizontal = len(array[0])
x = 0
count = 0

for y in range(0, len(array)):
    if array[y][x] == '#':
        count += 1
    x = (x + 3) % len_horizontal

print(count)
