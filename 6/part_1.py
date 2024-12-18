from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    def next(self):
        return Direction((self.value + 1) % 4)

layout = []
guardx = 0
guardy = 0
facing = Direction.UP
visited_count = 0

def in_bounds(x, y):
    return x >= 0 and \
        x < len(layout[0]) and \
        y >= 0 and \
        y < len(layout)

def move(x, y):
    if in_bounds(x, y) and layout[y][x] == '#':
        # rotate clockwise
        global facing
        facing = facing.next()
    else:
        global guardx
        global guardy
        guardx = x
        guardy = y


with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        layout.append(line)

        #check if this line contains the guard
        x = line.find('^')
        if x > -1:
            guardx = x
            guardy = len(layout)-1

while in_bounds(guardx, guardy):
    print(guardx, guardy, facing)
    # have we seen this spot before?
    if layout[guardy][guardx] != 'X':
        visited_count+=1
        layout[guardy] = layout[guardy][:guardx] + \
            'X' + layout[guardy][guardx+1:]


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

print(visited_count)