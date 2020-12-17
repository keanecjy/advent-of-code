def is_lower(x):
    return x == 'F' or x == 'L'


def binary_search(string):
    str_len = len(string)
    start = 0
    end = pow(2, str_len) - 1
    # print(end)
    for i in range(0, str_len - 1):
        c = string[i]
        half = (end - start + 1) / 2
        if is_lower(c):
            end -= half
        else:
            start += half

    last_char = string[str_len - 1]
    if is_lower(last_char):
        return start
    else:
        return end


def get_seat_id(line):
    row = binary_search(line[:7])
    col = binary_search(line[7:])
    return row * 8 + col


with open('Day05Input.txt', 'r') as f:
    data = f.read().split('\n')

curr_max = 0
curr_min = 999999999
total = 0

for line in data:
    seat_id = get_seat_id(line)
    total += seat_id
    curr_max = max(curr_max, seat_id)
    curr_min = min(seat_id, curr_min)


print(curr_max)

# Part 2
sum_expected = ((len(data) + 1) * (curr_max + curr_min)) / 2
print(sum_expected - total)
