# -*- coding: utf-8 -*-
flag = 0
with open('questions-words.txt','r') as f,open('family.txt','w') as g:
    for line in f:
        if flag != 0 and ': ' in line:
            break
        if line == ': family\n':
            flag += 1
        elif flag != 0:
            g.write(line)
