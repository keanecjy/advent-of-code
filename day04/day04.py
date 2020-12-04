f = open('Day04Input.txt', 'r')

string = ''
count = 0
ls = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')


def is_valid(word):
    for i in ls:
        if i not in word:
            return False
    return True


for line in f:
    if line == '\n':
        if is_valid(string):
            count += 1
        string = ''
    string += line

print(count)
