import string

fileName = '04_advent.txt'
backpacks_3 = []
score = 0

def readFile():
    global backpacksCompartment_1
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        string1 = line[:len(line)//2]
        string2 = line[len(line)//2:]
        backpacksCompartment_1.append(string1)
        backpacksCompartment_2.append(string2)
        print(backpacksCompartment_1)
        print(backpacksCompartment_2)

def compareBackpack(bp_1, bp_2):
    item = ''
    return item

def firstPart():
    global score
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
    readFile()



if __name__ == '__main__':
    firstPart()
    #secondPart()
    print('your score: ' + str(score))


