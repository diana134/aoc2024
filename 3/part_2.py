import re

def mul(x, y):
    return x*y

total = 0        
enabled = True
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()

        commands  = re.findall("((?:mul\(\d{1,3},\d{1,3}\))|(?:do\(\))|(?:don\'t\(\)))", line)
        for command in commands:
            if command == "do()":
                enabled = True
            elif command == "don't()":
                enabled = False
            elif enabled:
                total += eval(command)

print(total)
        
