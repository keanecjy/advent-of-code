f = open("Day02Input.txt", "r")


def split_string(string):
    arr = string.split('-', 2)
    idx1 = int(arr[0])
    rem = arr[1].split(' ', 3)
    idx2 = int(rem[0])
    letter = rem[1][0]
    last = rem[2]

    return idx1 - 1, idx2 - 1, letter, last


def is_valid(string):
    idx1, idx2, letter, last = split_string(string)
    if last[idx1] == letter and last[idx2] == letter:
        return False
    return last[idx1] == letter or last[idx2] == letter


num = 0

for line in f:
    if is_valid(line):
        num += 1

print(num)
