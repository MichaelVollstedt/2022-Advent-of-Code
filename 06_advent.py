import time
from collections import deque
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
    size = 14
    i = 0
    y = 13 + 1
    for c in line:
        check_buffer = line[i:y]
        sqnc = list(set(check_buffer))
        if len(sqnc) == size:
            break
        else:
            i += 1
            y += 1

    return y

def get_opt_message_endpoint(line):
    size = 14
    i = 0
    y = 13 + 1
    while y <= len(line):
        if len(set(line[i:y])) == size:
            return y
        else:
            y += 1
            i += 1

    return -1

def get_opt_2_message_endpoint(line):
    for i in range(14, len(line)-1):
        if len(set(line[i-14:i])) == 14:
            return i
    return -1

def get_deque_message_endpoint(line):
    window = deque(maxlen=14)
    for idx, char in enumerate(line, 1):
        window.append(char)
        if len(set(window)) == 14:
            return idx
    return -1

def firstPart():
    line = readFile()
    st = time.time()
    end = get_buffer_endpoint(line)
    et = time.time()
    print('The end of unique code = ' + str(end))

    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')



def secondPart():
    line = readFile()
    st = time.time()
    end = get_message_endpoint(line)
    et = time.time()
    print('The end of unique code (badly implemented) = ' + str('?'))
    elapsed_time = (et - st) * 1000
    print('Execution time (badly implemented):', elapsed_time, 'milli-seconds')

    st = time.time()
    end = get_opt_message_endpoint(line)
    et = time.time()
    print('The end of unique code (window) = ' + str('?'))
    elapsed_time = (et - st) * 1000
    print('Execution time (window):', elapsed_time, 'milli-seconds')

    st = time.time()
    end = get_opt_2_message_endpoint(line)
    et = time.time()
    print('The end of unique code (window-optimized) = ' + str('?'))
    elapsed_time = (et - st) * 1000
    print('Execution time (window-optimized):', elapsed_time, 'milli-seconds')

    signal = open("06_advent.txt").read()
    st = time.time()
    end = get_deque_message_endpoint(signal)
    et = time.time()
    print('The end of unique code (deque) = ' + str('?'))
    elapsed_time = (et - st) * 1000
    print('Execution time (deque):', elapsed_time, 'milli-seconds')

if __name__ == '__main__':
    #firstPart()
    secondPart()
