def get_number_of_trees(dx, dy):
    x = 0
    count = 0

    for y in range(0, len(array), dy):
        if array[y][x] == '#':
            count += 1
        x = (x + dx) % len_horizontal
    return count


with open('Day03Input.txt', 'r') as f:
    data = f.read()

array = data.split('\n')
len_horizontal = len(array[0])
access_array = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
val = 1

for i in access_array:
    val = val * get_number_of_trees(i[0], i[1])

print(val)
