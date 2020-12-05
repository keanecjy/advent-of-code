def split_string(string):
    arr = string.split('-', 2)
    first = int(arr[0])
    rem = arr[1].split(' ', 3)
    second = int(rem[0])
    letter = rem[1][0]
    last = rem[2]

    return first, second, letter, last


def has_sufficient_letters(string):
    first, second, letter, string = split_string(string)
    count = 0
    for x in string:
        if x == letter:
            count += 1

    return first <= count <= second


f = open("Day02Input.txt", "r")
num = 0

for line in f:
    if has_sufficient_letters(line):
        num += 1

print(num)
