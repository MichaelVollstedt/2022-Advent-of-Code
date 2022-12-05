import string

fileName = '05_advent.txt'
numberOfSubsets = 0
words = []

def readFile():
    stacks = []
    words = []
    lines = open(fileName, 'r')

    #add crates
    for line in lines:
        stack = []
        for c in line.strip():
            if c.isalpha():
                stack.append(c)
        stacks.append(stack)

        #add instructions
        words.append(line.strip().split())

    return stacks, words


def firstPart():
    stacks, words = readFile()

    for word in words:
        if not word:
            print('empty')
        elif word[0] == 'move':
            # Find the source and destination stacks
            num_crates = int(word[1])
            src_stack = int(word[3]) - 1
            dst_stack = int(word[5]) - 1
            n = num_crates
            for i in range(n):
                # Remove the top crate from the source stack and append it to the
                # destination stack
                crate = stacks[src_stack].pop()
                stacks[dst_stack].append(crate)

    # Print the top crate of each stack
    for stack in stacks:
        print(stack[-1])


def secondPart():
    f = open('05_advent.txt', mode='r')

    line = f.readline()

    row = [line[i * 4 + 1] for i in range(len(line) // 4)]
    crates = [[] for i in range(len(row))]

    while row[0].isalpha() or row[0] == ' ':
        crates = [crates[i] + [row[i]] if row[i] != ' ' else [] for i in range(len(crates))]
        line = f.readline()
        row = [line[i * 4 + 1] for i in range(len(line) // 4)]

    crates2 = crates.copy()
    f.readline()
    commands = [line.split(' ') for line in f]
    for command in commands:
        quantity = int(command[1])
        source = int(command[3]) - 1
        target = int(command[5]) - 1
        to_move = crates[source][:quantity]
        crates[source] = crates[source][quantity:]
        to_move.reverse()
        crates[target] = to_move + crates[target]

    print(f"First solution: {''.join([crate[0] for crate in crates])}")

    for command in commands:
        quantity = int(command[1])
        source = int(command[3]) - 1
        target = int(command[5]) - 1
        to_move = crates2[source][:quantity]
        crates2[source] = crates2[source][quantity:]
        crates2[target] = to_move + crates2[target]

    print(f"Second solution: {''.join([crate[0] for crate in crates2])}")

if __name__ == '__main__':
    #firstPart()
    secondPart()
