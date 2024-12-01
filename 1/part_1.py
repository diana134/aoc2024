list1 = []
list2 = []
total_distance = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        list1.append(int(tokens[0]))
        list2.append(int(tokens[1]))

list1.sort()
list2.sort()

for i in range(len(list1)):
    diff = abs(list1[i] - list2[i])
    total_distance += diff

print(total_distance)