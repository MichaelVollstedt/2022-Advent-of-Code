# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
fileName = '02_advent.txt'
elf = []
me = []
score = 0

def readFile():
    global elf, me
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        print(line)
        elf.append(line[0])
        me.append(line[2])

def firstPart():
    global score
    i = 0

    readFile()
    print(elf)
    print(me)

    for hand in me:
        checkResult(elf[i], hand)
        i += 1

def checkResult(elfHand, meHand):
    global score
    result = {'AX':4, 'BX':1, 'CX':7, 'AY': 8, 'BY': 5,'CY': 2, 'AZ': 3, 'BZ': 9, 'CZ': 6}
    res = elfHand + meHand
    print('result for ' + res + ' = ' + str(result.get(res)))
    score += result.get(res)

        # 1 for Rock, 2 for Paper, and 3 for Scissors
        # elf: A for Rock, B for Paper, and C for Scissors
        # me:  X for Rock, Y for Paper, and Z for Scissors.

def checkHand(elfHand, outcome):
    # X means you need to lose,
    # Y means you need to end the round in a draw, and
    # Z means you need to win.

    result = {'AX': 'Z', 'BX': 'X', 'CX': 'Y', 'AY': 'X', 'BY': 'Y', 'CY': 'Z', 'AZ': 'Y', 'BZ': 'Z', 'CZ': 'X'}
    return result.get(elfHand+outcome)

def secondPart():
    global score
    i = 0

    readFile()

    for outcome in me:
        checkResult(elf[i], checkHand(elf[i], outcome))
        i += 1



if __name__ == '__main__':
    #firstPart()
    secondPart()
    print('your score: ' + str(score))


