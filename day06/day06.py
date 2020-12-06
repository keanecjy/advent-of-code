with open('Day06Input.txt', 'r') as f:
    data = f.read().split('\n\n')

count = 0

for answers in data:
    answers_trimmed = answers.replace('\n', '')
    hash_set = set()
    for char in answers_trimmed:
        hash_set.add(char)
    count += len(hash_set)

print(count)
