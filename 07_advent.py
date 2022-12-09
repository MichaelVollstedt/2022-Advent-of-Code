from collections import defaultdict
from itertools import accumulate

fileName = '09_advent.txt'

if __name__ == '__main__':
    # use defaultdict to add size to the same folder
    dirs = defaultdict(int)

    #
    for line in open(fileName):
        match line.split():
            # back to root
            case '$', 'cd', '/':
                curr = ['']
            # as we go back a folder, we also need to pop it out of our temp directory
            case '$', 'cd', '..':
                curr.pop()
            # add current folder to temp directory
            case '$', 'cd', x:
                curr.append(x)
            case '$', 'ls':
                pass
            case 'dir', _:
                pass
            #for root and every nested child we add the file size to the dict
            #accumulate will add values of the same key: thanks for that :)
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)
    #solution 1
    print(sum(s for s in dirs.values() if s <= 100_000))

    #solution 2
    print(min(s for s in dirs.values() if s >= dirs[''] - 40_000_000))
