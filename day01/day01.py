newList = list(open("Day01Input.txt", "r"))
newList = map(int, newList)
newList = sorted(newList)

sumNeeded = 2020
left = 0
right = len(newList) - 1


def getSum(left, right):
    while left < right:
        x = int(newList[left])
        y = int(newList[right])
        curr = x + y
        if curr == sumNeeded:
            return x, y
        elif curr < sumNeeded:
            left += 1
        else:  # curr > sumNeeded
            right -= 1


first, second = getSum(left, right)
print(first * second)

# Faster solution

from itertools import combinations

for a, b in combinations(newList, 2):
    if a + b == 2020:
        print(a * b)
        break
