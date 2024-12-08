import re

def mul(x, y):
    return x*y

total = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        
        commands  = re.findall("(mul\(\d{1,3},\d{1,3}\))", line)
        for command in commands:
            total += eval(command)

print(total)
        
