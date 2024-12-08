word_search = []
with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        word_search.append(line)

xmas_count = 0

def is_valid_index(x, y):
    return (y >= 0 and y < len(word_search)) and \
        (x >= 0 and x < len(word_search[y]))

def is_next_letter(x, y, c):
    return is_valid_index(x, y) and word_search[y][x] == c

for y, line in enumerate(word_search):
    for x, c in enumerate(line):
        if c == 'X':
            # this might be the start of an XMAS
            # look right
            if is_next_letter(x+1, y, "M") and \
                is_next_letter(x+2, y, "A") and \
                is_next_letter(x+3, y, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look down right
            if is_next_letter(x+1, y+1, "M") and \
                is_next_letter(x+2, y+2, "A") and \
                is_next_letter(x+3, y+3, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look down
            if is_next_letter(x, y+1, "M") and \
                is_next_letter(x, y+2, "A") and \
                is_next_letter(x, y+3, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look down left
            if is_next_letter(x-1, y+1, "M") and \
                is_next_letter(x-2, y+2, "A") and \
                is_next_letter(x-3, y+3, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look left
            if is_next_letter(x-1, y, "M") and \
                is_next_letter(x-2, y, "A") and \
                is_next_letter(x-3, y, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look up left
            if is_next_letter(x-1, y-1, "M") and \
                is_next_letter(x-2, y-2, "A") and \
                is_next_letter(x-3, y-3, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look up
            if is_next_letter(x, y-1, "M") and \
                is_next_letter(x, y-2, "A") and \
                is_next_letter(x, y-3, "S"):
                    # we found XMAS!
                    xmas_count+=1
            # look up right
            if is_next_letter(x+1, y-1, "M") and \
                is_next_letter(x+2, y-2, "A") and \
                is_next_letter(x+3, y-3, "S"):
                    # we found XMAS!
                    xmas_count+=1

print(xmas_count)