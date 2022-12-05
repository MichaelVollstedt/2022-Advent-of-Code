fileName = '05_advent.txt'

def readFile():
    lines = open(fileName, 'r')

    line = lines.readline()
    row = [line[i * 4 + 1] for i in range(len(line) // 4)]
    crates = [[] for i in range(len(row))]

    return crates

def firstPart():
    stacks = readFile()



def secondPart():
    stacks = readFile()


if __name__ == '__main__':
    firstPart()
    #secondPart()
