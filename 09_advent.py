fileName = '09_advent.txt'

def negative(x):
    neg = x * (-1)
    return neg

def readFile():
    # includes lists of x,y coordinates to from through the grid
    move_instructions = []

    # let's create the x,y input from the raw-data
    for line in open(fileName):
        li = line.strip().split()
        match li:
            # back to root
            case 'R', x:
                move_instructions.append([int(x), 0])
            case 'L', x:
                move_instructions.append([negative(int(x)), 0])
            case 'U', y:
                move_instructions.append([0, int(y)])
            case 'D', y:
                move_instructions.append([0, negative(int(y))])
    return move_instructions

# iteratively we need to move head forward and check if tail is still in touch or needs to be moved
def move_head_tails(move_x, move_y, head, tail, grid):
    # move right
    if move_x > 0:
        for i in range(move_x):
            head[0] += 1
            if not check_tails_touches(tail, head):
                tail = move_tails(tail, head, 'R')
            grid = mark_position_in_grid(grid, tail)
    # move left
    elif move_x < 0:
        for i in range(abs(move_x)):
            head[0] -= 1
            if not check_tails_touches(tail, head):
                tail = move_tails(tail, head, 'L')
            grid = mark_position_in_grid(grid, tail)
    # move up
    elif move_y > 0:
        for i in range(move_y):
            head[1] += 1
            if not check_tails_touches(tail, head):
                tail = move_tails(tail, head, 'U')
            grid = mark_position_in_grid(grid, tail)
    # move down
    elif move_y < 0:
        for i in range(abs(move_y)):
            head[1] -= 1
            if not check_tails_touches(tail, head):
                tail = move_tails(tail, head, 'D')
            grid = mark_position_in_grid(grid, tail)
    return grid, head, tail

# check if the tail touches the head, if not we need to move it
def check_tails_touches(tail, head):
    if abs(tail[0]-head[0]) > 1 or abs(tail[1]-head[1]) > 1:
        return False
    return True

def move_tails(tail, head, direction):
    match direction:
        case 'L':
            match relative_position_head_to_tail_horizontally(head, tail):
                case 'U':
                    tail[0] -= 1
                    tail[1] += 1
                    return tail
                case 'D':
                    tail[0] -= 1
                    tail[1] -= 1
                    return tail
                case 'M':
                    tail[0] -= 1
                    return tail
        case 'R':
            match relative_position_head_to_tail_horizontally(head, tail):
                case 'U':
                    tail[0] += 1
                    tail[1] += 1
                    return tail
                case 'D':
                    tail[0] += 1
                    tail[1] -= 1
                    return tail
                case 'M':
                    tail[0] += 1
                    return tail
        case 'U':
            match relative_position_head_to_tail_vertically(head, tail):
                case 'L':
                    tail[0] -= 1
                    tail[1] += 1
                    return tail
                case 'R':
                    tail[0] += 1
                    tail[1] += 1
                    return tail
                case 'M':
                    tail[1] += 1
                    return tail
        case 'D':
            match relative_position_head_to_tail_vertically(head, tail):
                case 'L':
                    tail[0] -= 1
                    tail[1] -= 1
                    return tail
                case 'R':
                    tail[0] += 1
                    tail[1] -= 1
                    return tail
                case 'M':
                    tail[1] -= 1
                    return tail

def relative_position_head_to_tail_vertically(head, tail):
    # head is right of tail
    if head[0] - tail[0] > 0:
        return 'R'
    # head is left of tail
    elif head[0] - tail[0] < 0:
        return 'L'
    # head is directly above tail
    elif head[0] - tail[0] == 0:
        return 'M'
    return 'ERROR'

def relative_position_head_to_tail_horizontally(head, tail):
    # head is above tail
    if head[1] - tail[1] > 0:
        return 'U'
    # head is below tail
    elif head[1] - tail[1] < 0:
        return 'D'
    # head is middle of tail
    elif head[1] - tail[1] == 0:
        return 'M'
    return 'ERROR'

def mark_position_in_grid(grid, tail):
    # transformation of coordinates between tail and grid
    x = tail[0]
    y = tail[1]
    #length = len(grid)
    # length - 1 if we start at an edge
    #y = length - tail[1]
    grid[y][x] = '#'

    return grid

def count_tails(grid):
    c = 0
    for line in grid:
        for val in line:
            if val == '#':
                c +=1
    return c

def firstPart():
    rows, cols = (5000, 5000)
    grid = [[0 for i in range(cols)] for j in range(rows)]
    move_instructions = readFile()
    head = [2500,2500]
    tail = [2500,2500]

    for cord in move_instructions:
        grid, head, tail = move_head_tails(cord[0], cord[1], head, tail, grid)

    for s in grid:
        print(str(s) + '\n')

    c = count_tails(grid)
    print(c)

# iteratively we need to move head forward and check if tail is still in touch or needs to be moved
def move_head_tails_9(move_x, move_y, knots, grid):
    # move right
    if move_x > 0:
        for y in range(move_x):
            knots[0][0] += 1
            for i in range(len(knots) - 1):
                if not check_tails_touches(knots[i+1], knots[i]):
                    knots[i+1] = move_tails(knots[i+1], knots[i], 'R')
                if i == len(knots) - 2:
                    grid = mark_position_in_grid(grid, knots[i+1])
    # move left
    elif move_x < 0:
        for y in range(abs(move_x)):
            knots[0][0] -= 1
            for i in range(len(knots) - 1):
                if not check_tails_touches(knots[i+1], knots[i]):
                    tail = move_tails(knots[i+1], knots[i], 'L')
                if i == len(knots) - 2:
                    grid = mark_position_in_grid(grid, knots[i+1])
    # move up
    elif move_y > 0:
        for y in range(move_y):
            knots[0][1] += 1
            for i in range(len(knots) - 1):
                if not check_tails_touches(knots[i+1], knots[i]):
                    tail = move_tails(knots[i+1], knots[i], 'U')
                if i == len(knots) - 2:
                    grid = mark_position_in_grid(grid, knots[i+1])
    # move down
    elif move_y < 0:
        for y in range(abs(move_y)):
            knots[0][1] -= 1
            for i in range(len(knots) - 1):
                if not check_tails_touches(knots[i+1], knots[i]):
                    tail = move_tails(knots[i+1], knots[i], 'D')
            if i == len(knots) - 2:
                grid = mark_position_in_grid(grid, knots[i+1])
    return grid, knots[i], knots[i+1]


def secondPart():
    rows, cols = (40, 40)
    grid = [['.' for i in range(cols)] for j in range(rows)]
    move_instructions = readFile()
    knot_count = 10
    knots = [[20, 20] for i in range(knot_count)]

    for cord in move_instructions:
        grid, head, tail = move_head_tails_9(cord[0], cord[1], knots, grid)

    for s in grid:
        print(str(s) + '\n')

    c = count_tails(grid)
    print(c)



if __name__ == '__main__':
    #firstPart()
    secondPart()
