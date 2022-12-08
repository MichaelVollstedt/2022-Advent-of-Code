fileName = '08_advent.txt'

def readFile():
    lines = open(fileName, 'r')
    array = []
    for line in lines:
        line = line.strip()
        array.append([int(s) for s in line])
    return array



def check_horizontal_back(field, x,y, cur_val):
    tree = True
    print('hor_bac: x = ' + str(x) + ' y = ' + str(y))
    # check all horizontal trees and return true if it stays the biggest
    if x <= 0:
        return True

    if x-1 >= 0:
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y][x-1]:
            return False
        else:
            tree = check_horizontal_back(field, x-1, y, cur_val)

        return tree
    return tree


def check_horizontal_fwd(field, x,y, cur_val):
    tree = True
    print('hor_fwd: x = ' + str(x) + ' y = ' + str(y))
    # check all horizontal trees and return true if it stays the biggest
    if x >= len(field[0]):
        return True

    if x+1 <= len(field[0])-1:
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y][x+1]:
            return False
        else:
            tree = check_horizontal_fwd(field, x+1, y, cur_val)

        return tree
    return tree


def check_vertical_up(field, x,y, cur_val):
    tree = True
    print('ver_up : x = ' + str(x) + ' y = ' + str(y))
    # check all horizontal trees and return true if it stays the biggest
    if y <= 0:
        return True

    if y-1 >= 0:
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y-1][x]:
            return False
        else:
            tree = check_horizontal_back(field, x, y-1, cur_val)
        return tree
    return tree

def check_vertical_down(field, x,y, cur_val):
    tree = True
    print('ver_dow: x = ' + str(x) + ' y = ' + str(y))
    # check all horizontal trees and return true if it stays the biggest
    if y >= len(field)-1:
        return True

    if y+1 <= len(field):
        # check if tree is bigger than previous horizontal left
        if cur_val <= field[y+1][x]:
            return False
        else:
            tree = check_horizontal_back(field, x, y+1, cur_val)
        return tree
    return tree


def firstPart():
    array = readFile()
    count = 0

    for y, y_li in enumerate(array, 0):
        for x, x_val in enumerate(y_li, 0):
            tree = False
            tree = check_horizontal_back(array, x, y, x_val)
            print(tree)
            if not tree:
                tree = check_horizontal_fwd(array, x, y, x_val)
                print(tree)
            if not tree:
                tree = check_vertical_up(array, x, y, x_val)
                print(tree)
            if not tree:
                tree = check_vertical_down(array, x, y, x_val)
                print(tree)
            if tree:
                count += 1
                print(count)
            #print('x = ' + str(x) + ' y = ' + str(y))

    print('total count = ' + str(count))




def secondPart():
    stacks = readFile()


if __name__ == '__main__':
    firstPart()
    #secondPart()
