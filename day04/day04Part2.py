import re


def is_within_range(number, start, end):
    return re.fullmatch('^[1-9]\\d*', number) and start <= int(number) <= end


def is_valid_arr(arr):
    return len(arr) == 2 and arr[1] == ''


def is_valid_height(height):
    cm = height.split('cm')
    inches = height.split('in')
    return (
        (is_valid_arr(cm) and is_within_range(cm[0], 150, 193))
        ^ (is_valid_arr(inches) and is_within_range(inches[0], 59, 76)))


validityMapping = {
    'byr': lambda x: is_within_range(x, 1920, 2002),
    'iyr': lambda x: is_within_range(x, 2010, 2020),
    'eyr': lambda x: is_within_range(x, 2020, 2030),
    'hgt': lambda x: is_valid_height(x),
    'hcl': lambda x: re.fullmatch('#[0-9|a-f]{6}', x),
    'ecl': lambda x: re.fullmatch('amb|blu|brn|gry|grn|hzl|oth', x),
    'pid': lambda x: re.fullmatch('[0-9]{9}', x)
}


def is_valid(word):
    arr = word.strip().replace('\n', ' ').split(' ')
    mapping = {}
    for item in arr:
        map_array = item.split(':')
        mapping[map_array[0]] = map_array[1]

    for i in validityMapping.keys():
        if i not in mapping or not validityMapping[i](mapping[i]):
            return False
    return True


with open('Day04Input.txt', 'r') as f:
    data = f.read()

count = 0
array = data.split('\n\n')
for passport in array:
    if is_valid(passport):
        count += 1

print(count)
