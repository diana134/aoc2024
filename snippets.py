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

# check if list2 contains any items from list1
any(x in list1 for x in list2)


# custom sorting
import functools 
def mycmp(a, b): 
    print("comparing ", a, " and ", b) 
    if a > b: 
        return 1
    elif a < b: 
        return -1
    else: 
        return 0
print(sorted([1, 2, 4, 2], key=functools.cmp_to_key(mycmp))) 