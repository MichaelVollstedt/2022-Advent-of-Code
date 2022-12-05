fileName = '05_advent.txt'

def readFile():
    lines = open(fileName, 'r')

    #read first line and generate list structure. Keep in mind we only need the creates.
    #Hence only every fourth char needed
    line = lines.readline()
    row = [line[i * 4 + 1] for i in range(len(line) // 4)]
    crates = [[] for i in range(len(row))]

    #get row-input and write it to crates. Update next row until line with numbers is hit
    while row[0].isalpha() or row[0] == ' ':
        crates = [crates[i] + [row[i]] if row[i] != ' ' else [] for i in range(len(crates))]
        line = lines.readline()
        row = [line[i * 4 + 1] for i in range(len(line) // 4)]

    #get the rest of the input, after lines hit '\n'
    lines.readline()
    moveSets = [line.strip().split() for line in lines]

    return crates, moveSets

def moveCrates(stacks, moveSets):

    for move in moveSets:
        count = int(move[1])
        src_stack = int(move[3]) - 1
        dst_stack = int(move[5]) - 1
        i = 0
        for i in range(count):
            val = stacks[src_stack][0]
            stacks[src_stack].pop(0)
            stacks[dst_stack].insert(0, val)

            i += 1

    return stacks

def moveMultipleCrates(stacks, moveSets):
    i = 0
    for move in moveSets:
        i += 1
        count = int(move[1])
        src_stack = int(move[3]) - 1
        dst_stack = int(move[5]) - 1
        val = stacks[src_stack][:count]
        stacks[src_stack] = stacks[src_stack][count:]
        stacks[dst_stack] = val + stacks[dst_stack]

    print('Number of moves = ' + str(i))


def firstPart():
    stacks, moveSets = readFile()
    print(stacks)
    print(moveSets)
    moveCrates(stacks, moveSets)
    print(stacks)
    str = ''
    for stack in stacks:
        if bool(stack):
            str += stack[0]
    print(str)


def secondPart():
    stacks, moveSets = readFile()
    print(stacks)
    print(moveSets)
    moveMultipleCrates(stacks, moveSets)
    print(stacks)
    str = ''
    for stack in stacks:
        if bool(stack):
            str += stack[0]
    print(str)


if __name__ == '__main__':
    #firstPart()
    secondPart()
