# basic file input
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        # TODO process line
        
# is sorted ascending
all(int(data[i]) <= int(data[i + 1]) for i in range(len(data) - 1))

# is sorted descending
all(int(data[i]) >= int(data[i + 1]) for i in range(len(data) - 1))