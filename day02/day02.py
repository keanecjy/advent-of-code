f = open("Day02Input.txt", "r")


def splitString(string):
    arr = string.split('-', 2)
    first = int(arr[0])
    rem = arr[1].split(' ', 3)
    second = int(rem[0])
    letter = rem[1][0]
    last = rem[2]

    return first, second, letter, last


def hasSufficientLetter(line):
    first, second, letter, string = splitString(line)
    count = 0
    for x in string:
        if x == letter:
            count += 1

    return first <= count <= second


num = 0

for line in f:
    if hasSufficientLetter(line):
        num += 1

print(num)
