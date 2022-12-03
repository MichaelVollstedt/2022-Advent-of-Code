# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
fileName = '01_advent.txt'
sumCal = []

def readFile():
    global sumCal
    sum = 0
    lines = open(fileName, 'r')

    for line in lines:
        line = line.strip()
        print(line)
        if line != '':
            line = int(line)
            sum += line
        if line == '':
            sumCal.append(sum)
            sum = 0

def firstPart():
    readFile()
    sumCal.sort()
    print(sumCal)
    print(sumCal[-1])

def secondPart():
    readFile()
    sumCal.sort()
    print(sumCal)
    top3 = sumCal[-3] + sumCal[-2] + sumCal[-1]
    print(top3)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #firstPart()
    secondPart()


