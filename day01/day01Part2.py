new_list = list(open("Day01Input.txt", "r"))
new_list = map(int, new_list)
new_list = sorted(new_list)

total = 2020
length = len(new_list) - 1


def get_sum(left, right, sum_needed):
    while left < right:
        first = new_list[left]
        second = new_list[right]
        curr = first + second
        if curr == sum_needed:
            return first, second
        elif curr < sum_needed:
            left += 1
        else:  # curr > sum_needed
            right -= 1
    return -1, -1


for i in range(0, length - 2):
    current = new_list[i]
    two_sum = total - current
    (x, y) = get_sum(i + 1, length, two_sum)
    if x != -1:
        print(current * x * y)

# Faster solution

from itertools import combinations

for a, b, c in combinations(new_list, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break
