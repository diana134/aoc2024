def is_sorted(data):
    return all(int(data[i]) <= int(data[i + 1]) for i in range(len(data) - 1)) or \
        all(int(data[i]) >= int(data[i + 1]) for i in range(len(data) - 1))

def valid_increment(a, b):
    diff = a - b
    return abs(diff) > 0 and abs(diff) <= 3

safe_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        
        is_safe = True

        if not is_sorted(tokens):
            is_safe = False

        for i in range(len(tokens) - 1):
            if not valid_increment(int(tokens[i]), int(tokens[i+1])):
                is_safe = False

        if is_safe: 
            safe_count += 1

print(safe_count)