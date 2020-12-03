newList = list(open("Day01Input.txt", "r"))
newList = map(int, newList)
newList = sorted(newList)

totalSum = 2020
right = len(newList) - 1


def getSum(left, right, sumNeeded):
    while left < right:
        x = newList[left]
        y = newList[right]
        curr = x + y
        if curr == sumNeeded:
            return x, y
        elif curr < sumNeeded:
            left += 1
        else:  # curr > sumNeeded
            right -= 1
    return -1, -1


for i in range(0, right - 2):
    current = newList[i]
    twoSum = totalSum - current
    (x, y) = getSum(i + 1, right, twoSum)
    if x != -1:
        print(current * x * y)

# Faster solution

from itertools import combinations

for a, b, c in combinations(newList, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break
