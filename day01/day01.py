f = open("Day01Input.txt", "r")
new_list = list(map(int, f))

sum_needed = 2020
hash_set = set()

for i in new_list:
    value = sum_needed - i
    if value in hash_set:
        print(i * value)
    hash_set.add(i)

# Faster solution
from itertools import combinations

for a, b in combinations(new_list, 2):
    if a + b == 2020:
        print(a * b)
