def is_valid(word):
    for i in ls:
        if i not in word:
            return False
    return True


ls = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

with open('Day04Input.txt', 'r') as f:
    data = f.read()

count = 0
array = data.split('\n\n')
for passport in array:
    if is_valid(passport):
        count += 1

print(count)
