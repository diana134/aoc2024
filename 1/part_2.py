list1 = []
hash2 = {}
total_similarity = 0

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        tokens = line.split()
        list1.append(int(tokens[0]))
        if tokens[1] in hash2.keys():
            hash2[tokens[1]] += 1
        else:
            hash2[tokens[1]] = 1

for i in range(len(list1)):
    num = list1[i]
    if str(num) in hash2.keys():
        hash2_occurances = hash2[str(num)]
        total_similarity += num * hash2_occurances

print(total_similarity)