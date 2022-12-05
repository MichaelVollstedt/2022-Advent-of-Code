import string

fileName = '05_advent.txt'
numberOfSubsets = 0
words = []

def readFile():
    stacks_1 = []
    stacks_2 = []
    stacks_3 = []
    stacks_4 = []
    stacks_5 = []
    stacks_6 = []
    stacks_7 = []
    stacks_8 = []
    stacks_9 = []
    words = []
    words_all = []

    lines = open(fileName, 'r')

    line = lines.readline()
    row = [line[i * 4 + 1] for i in range(len(line) // 4)]
    crates = [[] for i in range(len(row))]

    #add crates
    for i, line in enumerate(lines):
        stack_1 = ''
        stack_2 = ''
        stack_3 = ''
        stack_4 = ''
        stack_5 = ''
        stack_6 = ''
        stack_7 = ''
        stack_8 = ''
        stack_9 = ''

        x = len(line)
        sp = line.strip()
        if not sp:
            break
        if line[1].isalpha():
            stack_1 = line[1]
        if line[5].isalpha():
            stack_2 = line[5]
        if line[9].isalpha():
            stack_3 = line[9]
        if line[13].isalpha():
            stack_4 = line[13]
        if line[17].isalpha():
            stack_5 = line[17]
        if line[21].isalpha():
            stack_6 = line[21]
        if line[25].isalpha():
            stack_7 = line[25]
        if line[29].isalpha():
            stack_8 = line[29]
        if line[33].isalpha():
            stack_9 = line[33]

        if bool(stack_1):
            stacks_1.append(stack_1)
        if bool(stack_2):
            stacks_2.append(stack_2)
        if bool(stack_3):
            stacks_3.append(stack_3)
        if bool(stack_4):
            stacks_4.append(stack_4)
        if bool(stack_5):
            stacks_5.append(stack_5)
        if bool(stack_6):
            stacks_6.append(stack_6)
        if bool(stack_7):
            stacks_7.append(stack_7)
        if bool(stack_8):
            stacks_8.append(stack_8)
        if bool(stack_9):
            stacks_9.append(stack_9)

    for line in lines:
        words.append(line.strip().split())

    stacks = [stacks_1, stacks_2, stacks_3, stacks_4, stacks_5, stacks_6, stacks_7, stacks_8, stacks_9]
    return stacks, words

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
