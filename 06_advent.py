import time
from collections import deque, Counter
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

def get_window_smart_message_endpoint(line):
    # line needs to be a string
    i = 14
    line_len = len(line)
    while i <= line_len-1:
        window = line[i-14:i]
        if len(set(window)) == 14:
            return i
        else:
            collection = Counter(window)
            # check for multiple occurrences
            not_unique = [value > 1 for value in collection.values()]
            # get index of duplicates
            dub_list = [y for y, x in enumerate(not_unique) if x == True]
            # get char of the duplicates
            keys = list(collection.keys())
            alpha_list = []
            for idx in dub_list:
                alpha_list.append(keys[int(idx)])
            # get all positions of char
            key_pos_dict = {}
            for char in alpha_list:
                x = 0
                found = []
                while x < len(window):
                    x = window.find(char, x)
                    if x == -1:
                        break
                    found.append(x)
                    x += 1
                found.sort()
                key_pos_dict[char] = found

            # get highest index of duplicate
            idx_dup = 0
            high_key = ''
            for k, v in key_pos_dict.items():
                max_value = max(v)
                if max_value > idx_dup:
                    idx_dup = max_value
                    high_key = k

            # finally, get second backward position of duplicate char
            high_value = key_pos_dict[high_key]
            second_high = high_value[-2]
            # always get the next index of the second last high index (might be the same,
            # if both char are next to each-other
            next_idx = second_high
            if next_idx < line_len-1-14:
                i += next_idx + 1
                #print(i)
            else:
                i = line_len-1-14
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
    print('The end of unique code (badly implemented) = ' + str(end))
    elapsed_time = (et - st) * 1000
    print('Execution time (badly implemented):', elapsed_time, 'milli-seconds')

    st = time.time()
    end = get_opt_message_endpoint(line)
    et = time.time()
    print('The end of unique code (window) = ' + str(end))
    elapsed_time = (et - st) * 1000
    print('Execution time (window):', elapsed_time, 'milli-seconds')

    st = time.time()
    end = get_opt_2_message_endpoint(line)
    et = time.time()
    print('The end of unique code (window-optimized) = ' + str(end))
    elapsed_time = (et - st) * 1000
    print('Execution time (window-optimized):', elapsed_time, 'milli-seconds')

    signal = open("06_advent.txt").read()
    st = time.time()
    end = get_deque_message_endpoint(signal)
    et = time.time()
    print('The end of unique code (deque) = ' + str(end))
    elapsed_time = (et - st) * 1000
    print('Execution time (deque):', elapsed_time, 'milli-seconds')

    st = time.time()
    end = get_window_smart_message_endpoint(signal)
    et = time.time()
    print('The end of unique code (find algo) = ' + str(end))
    elapsed_time = (et - st) * 1000
    print('Execution time (find algo):', elapsed_time, 'milli-seconds')

if __name__ == '__main__':
    #firstPart()
    secondPart()
