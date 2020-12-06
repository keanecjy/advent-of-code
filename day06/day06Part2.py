with open('Day06Input.txt', 'r') as f:
    data = f.read().split('\n\n')

count = 0

for answers in data:
    array = answers.split('\n')
    size = len(array)
    hash_map = dict()
    for answer in array:
        for char in answer:
            hash_map[char] = hash_map[char] + 1 if char in hash_map else 1
    for (key, val) in hash_map.items():
        if val == size:
            count += 1

print(count)
