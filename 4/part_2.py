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
        if c == 'A':
            # this might be the center of an X-MAS

            # upper left is M and lower right is S
            # OR
            # upper left is S and lower right is M

            # AND

            # lower left is M and upper right is S
            # OR
            # lower left is S and upper right is M
            if ( \
                    (is_next_letter(x-1, y-1, "M") and \
                        is_next_letter(x+1, y+1, "S")) or \
                    (is_next_letter(x-1, y-1, "S") and \
                        is_next_letter(x+1, y+1, "M")) \
                ) and \
                (
                    (is_next_letter(x-1, y+1, "M") and \
                        is_next_letter(x+1, y-1, "S")) or \
                    (is_next_letter(x-1, y+1, "S") and \
                        is_next_letter(x+1, y-1, "M")) \
                ):
                xmas_count+=1

print(xmas_count)