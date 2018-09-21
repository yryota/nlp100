# -*- coding: utf-8 -*-
def check(fname):
    with open(fname,'r') as f:
        n_correct = 0
        n_line = 0
        for line in f:
            word = line[:-1].split(' ')
            ans = word[3]
            pred = word[4]
            n_line += 1
            if ans == pred:
                n_correct += 1
    print(n_correct/n_line)

if __name__ == '__main__':
    check('85out.txt')
    check('90out.txt')
