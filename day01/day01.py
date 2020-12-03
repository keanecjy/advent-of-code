newList = list(open("Day01Input.txt", "r"))
newList = list(map(int, newList))

sumNeeded = 2020
hashSet = set()

for i in newList :
    value = sumNeeded - i
    if value in hashSet:
        print(i * value)
    hashSet.add(i)

# Faster solution
from itertools import combinations

for a, b in combinations(newList, 2):
    if a + b == 2020:
        print(a * b)
