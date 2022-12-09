fileName = '08_advent.txt'
max = []

def readFile():
    lines = open(fileName, 'r')
    array = []
    for line in lines:
        line = line.strip()
        array.append([int(s) for s in line])
    return array



def check_horizontal_back(field, x,y, cur_val, score):
    tree = True
    print('hor_bac: x = ' + str(x) + ' y = ' + str(y))
    # check all horizontal trees and return true if it stays the biggest
    if x <= 0:
        return True, score

    if x-1 >= 0:
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y][x-1]:
            score += 1
            return False, score
        else:
            score += 1
            tree, score = check_horizontal_back(field, x-1, y, cur_val, score)

        return tree, score
    return tree, score


def check_horizontal_fwd(field, x,y, cur_val, score):
    tree = True
    print('hor_fwd: x = ' + str(x) + ' y = ' + str(y))
    # check all next horizontal trees and return true if it stays the biggest
    if x >= len(field[0]):
        return True, score

    if x+1 <= len(field[0])-1:
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y][x+1]:
            score += 1
            return False, score
        else:
            score += 1
            tree, score = check_horizontal_fwd(field, x+1, y, cur_val, score)

        return tree, score
    return tree, score


def check_vertical_up(field, x,y, cur_val, score):
    tree = True
    print('ver_up : x = ' + str(x) + ' y = ' + str(y))
    # check all upper vertical trees and return true if it stays the biggest
    if y <= 0:
        return True, score

    if y-1 >= 0:
        if cur_val <= field[y-1][x]:
            score += 1
            return False, score
        else:
            score += 1
            tree, score = check_vertical_up(field, x, y-1, cur_val, score)
        return tree, score
    return tree, score

def check_vertical_down(field, x,y, cur_val, score):
    tree = True
    print('ver_dow: x = ' + str(x) + ' y = ' + str(y))
    # check all bottom vertical trees and return true if it stays the biggest
    if y >= len(field)-1:
        return True, score

    if y+1 <= len(field):
        if cur_val <= field[y+1][x]:
            score += 1
            return False, score
        else:
            score += 1
            tree, score = check_vertical_down(field, x, y+1, cur_val, score)
        return tree, score
    return tree, score


def firstPart():
    array = readFile()
    count = 0

    for y, y_li in enumerate(array, 0):
        for x, x_val in enumerate(y_li, 0):
            tree = False
            tree, score = check_horizontal_back(array, x, y, x_val, -1)
            print(tree)
            if not tree:
                tree, score = check_horizontal_fwd(array, x, y, x_val, -1)
                print(tree)
            if not tree:
                tree, score = check_vertical_up(array, x, y, x_val, -1)
                print(tree)
            if not tree:
                tree, score = check_vertical_down(array, x, y, x_val, -1)
                print(tree)
            if tree:
                count += 1
                print(count)
            #print('x = ' + str(x) + ' y = ' + str(y))

    print('total count = ' + str(count))




def secondPart():
    max_val = []
    array = readFile()
    count = 0

    for y, y_li in enumerate(array, 0):
        for x, x_val in enumerate(y_li, 0):
            tree_score = []
            tree, tree_score_temp = check_horizontal_back(array, x, y, x_val, 0)
            tree_score.append(tree_score_temp)
            tree, tree_score_temp = check_horizontal_fwd(array, x, y, x_val, 0)
            tree_score.append(tree_score_temp)
            tree, tree_score_temp = check_vertical_up(array, x, y, x_val, 0)
            tree_score.append(tree_score_temp)
            tree, tree_score_temp = check_vertical_down(array, x, y, x_val, 0)
            tree_score.append(tree_score_temp)
            max_val.append(tree_score[0]*tree_score[1]*tree_score[2]*tree_score[3])

    max_val.sort()
    max_score = max_val[-1]
    print('max tree score = ' + str(max_score))

if __name__ == '__main__':
    #firstPart()
    secondPart()
