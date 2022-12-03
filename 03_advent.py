import string

fileName = '03_advent.txt'
backpacksCompartment_1 = []
backpacksCompartment_2 = []
backpacks_1 = []
backpacks_2 = []
backpacks_3 = []
score = 0

def readFile():
    global backpacksCompartment_1, backpacksCompartment_2
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        string1 = line[:len(line)//2]
        string2 = line[len(line)//2:]
        backpacksCompartment_1.append(string1)
        backpacksCompartment_2.append(string2)
        print(backpacksCompartment_1)
        print(backpacksCompartment_2)


def readFile2():
    global backpacks_1, backpacks_2, backpacks_3
    tempLines = []
    lines = open(fileName, 'r')
    i = 0
    y = 0

    for line in lines:
        line = line.strip()
        tempLines.append(line)

    n = len(tempLines) // 3

    for i in range(n):
        backpacks_1.append(tempLines[y])
        backpacks_2.append(tempLines[y+1])
        backpacks_3.append(tempLines[y+2])
        y += 3

    print(backpacks_1)
    print(backpacks_2)
    print(backpacks_3)

def compareBackpack(bp_1, bp_2):
    item = ''
    for char in bp_1:
        if char in bp_2:
            item = char
            break

    return item

def compareBackpack2(bp_1, bp_2, bp_3):
    item = ''
    for char in bp_1:
        if char in bp_2 and char in bp_3:
            item = char
            break

    return item

def itemScore(item):
    scoreItem = -1
    if item.islower():
        scoreItem = string.ascii_lowercase.find(item) + 1
    else:
        scoreItem = string.ascii_uppercase.find(item) + 27

    return scoreItem

    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.

def firstPart():
    global score, backpacksCompartment_1, backpacksCompartment_2
    i = 0
    readFile()
    n = len(backpacksCompartment_1)

    for i in range(n):
        resultItem = compareBackpack(backpacksCompartment_1[i], backpacksCompartment_2[i])
        print('Found identical backpack item: ' + str(resultItem))
        scorePerItem = int(itemScore(resultItem))
        print('score for item ' + str(resultItem) + ' is = ' + str(scorePerItem))
        score += scorePerItem


def secondPart():
    global score
    i = 0
    readFile2()
    n = len(backpacks_1)

    for i in range(n):
        resultItem = compareBackpack2(backpacks_1[i], backpacks_2[i], backpacks_3[i])
        print('Found identical backpack item: ' + str(resultItem))
        scorePerItem = int(itemScore(resultItem))
        print('score for item ' + str(resultItem) + ' is = ' + str(scorePerItem))
        score += scorePerItem



if __name__ == '__main__':
    #firstPart()
    secondPart()
    print('your score: ' + str(score))


