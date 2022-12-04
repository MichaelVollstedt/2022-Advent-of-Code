import string

fileName = '04_advent.txt'
numberOfSubsets = 0


def readFile():
    pairs = []
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        pairs.append(line)

    return pairs

def separate_range_string(range_string):
    # Split the string on the comma to get the two ranges
    ranges = range_string.split(',')

    # Create two empty lists to store our numbers
    numbers1 = []
    numbers2 = []

    # Loop through the ranges
    for i, r in enumerate(ranges):
        # Split the range on the dash to get the start and end of the range
        start, end = r.split('-')

        # Convert the start and end to integers
        start = int(start)
        end = int(end)

        # Add all the numbers in the range to the appropriate list
        if i == 0:
            numbers1.extend(range(start, end + 1))
        else:
            numbers2.extend(range(start, end + 1))

    # Return the two lists of numbers
    return numbers1, numbers2


def compareBackpack(bp_1, bp_2):
    item = ''
    return item

def checkForSubset(pairList):
    global numberOfSubsets

    for pair in pairList:
        elfA, elfB = separate_range_string(pair)
        if set(elfA).issubset(set(elfB)):
            numberOfSubsets += 1
            print('matching pair: ' + str(pair))
        elif set(elfB).issubset(set(elfA)):
            numberOfSubsets += 1
            print('matching pair: ' + str(pair))

def checkForIntersection(pairList):
    global numberOfSubsets

    for pair in pairList:
        elfA, elfB = separate_range_string(pair)
        if set(elfA).intersection(set(elfB)):
            numberOfSubsets += 1
            print('matching pair: ' + str(pair))

def firstPart():
    pairList = readFile()
    checkForSubset(pairList)


def secondPart():
    pairList = readFile()
    checkForIntersection(pairList)


if __name__ == '__main__':
    #firstPart()
    secondPart()
    print('your sub-set pairs: ' + str(numberOfSubsets))
