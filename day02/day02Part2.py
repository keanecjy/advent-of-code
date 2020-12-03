f = open("Day02Input.txt", "r")


def splitString(string):
    arr = string.split('-', 2)
    idx1 = int(arr[0])
    rem = arr[1].split(' ', 3)
    idx2 = int(rem[0])
    letter = rem[1][0]
    last = rem[2]

    return idx1 - 1, idx2 - 1, letter, last


def isValid(string):
    idx1, idx2, letter, last = splitString(string)
    if last[idx1] == letter and last[idx2] == letter:
        return False
    return last[idx1] == letter or last[idx2] == letter


num = 0

for line in f:
    if isValid(line):
        num += 1

print(num)
