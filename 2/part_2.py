from itertools import combinations

def is_sorted(data):
    return all(int(data[i]) <= int(data[i + 1]) for i in range(len(data) - 1)) or \
        all(int(data[i]) >= int(data[i + 1]) for i in range(len(data) - 1))

def valid_increment(a, b):
    diff = a - b
    return abs(diff) > 0 and abs(diff) <= 3

def is_report_safe(data):
    is_safe = True

    if not is_sorted(data):
        is_safe = False

    for i in range(len(data) - 1):
        if not valid_increment(int(data[i]), int(data[i+1])):
            is_safe = False

    return is_safe

safe_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()

        if is_report_safe(tokens): 
            safe_count += 1
        else:
            # remove 1 element at a time until safe or 
            # have tried all elements

            for c in combinations(tokens, len(tokens)-1):
                if is_report_safe(c):
                    safe_count += 1
                    break

print(safe_count)