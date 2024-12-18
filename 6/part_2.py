from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def next(self):
        return Direction((self.value + 1) % 4)

layout = []
startx = 0
starty = 0
guardx = 0
guardy = 0
facing = Direction.UP
visited_list = {}
loop_count = 0

def in_bounds(x, y):
    return x >= 0 and \
        x < len(layout[0]) and \
        y >= 0 and \
        y < len(layout)

def move(x, y):
    global guardx, guardy, facing

    if in_bounds(x, y) and layout[y][x] == '#':
        # rotate clockwise
        facing = facing.next()
    else:
        guardx = x
        guardy = y

def run():
    global layout, guardx, guardy, facing, visited_list, loop_count

    while in_bounds(guardx, guardy):
        # have we seen this spot before?
        if (guardx, guardy, facing) not in visited_list.keys():
            visited_list[(guardx, guardy, facing)] = True

            match facing:
                case Direction.UP:
                    move(guardx, guardy-1)
                case Direction.RIGHT:
                    move(guardx+1, guardy)
                case Direction.DOWN:
                    move(guardx, guardy+1)
                case Direction.LEFT:
                    move(guardx-1, guardy)
                case _:
                    print("wtf?")
                    break
        else:
            # we've been here facing this direction before,
            # therefore we're in a loop
            loop_count+=1
            break


with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        layout.append(line)

        #check if this line contains the guard
        x = line.find('^')
        if x > -1:
            startx = x
            starty = len(layout)-1

# change each character in the map to "#" and check for loops
for y, row in enumerate(layout):
    for i in range(len(row)):
        if row[i] != '#' and row[i] != '^':
            layout[y] = row[:i] + '#' + row[i+1:]
            
            run()

            # reset
            layout[y] = row[:i] + '.' + row[i+1:]
            guardx = startx
            guardy = starty
            facing = Direction.UP
            visited_list = {}


print(loop_count)