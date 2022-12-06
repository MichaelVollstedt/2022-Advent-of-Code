fileName = '06_advent.txt'

def readFile():
    lines = open(fileName, 'r')

    line = lines.readline()
    str = line.strip()
    c_list = [x for x in str]

    return c_list

def get_buffer_endpoint(line):
    i = 0
    y = 3 + 1
    for c in line:
        check_buffer = line[i:y]
        sqnc = list(set(check_buffer))
        if len(check_buffer) == len(sqnc):
            break
        else:
            i += 1
            y += 1

    return y

def get_message_endpoint(line):
    i = 0
    y = 13 + 1
    for c in line:
        check_buffer = line[i:y]
        sqnc = list(set(check_buffer))
        if len(check_buffer) == len(sqnc):
            break
        else:
            i += 1
            y += 1

    return y
def firstPart():
    line = readFile()
    end = get_buffer_endpoint(line)
    print('The end of unique code = ' + str(end))



def secondPart():
    line = readFile()
    end = get_message_endpoint(line)
    print('The end of unique code = ' + str(end))


if __name__ == '__main__':
    #firstPart()
    secondPart()
