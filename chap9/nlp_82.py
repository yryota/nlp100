# -*- coding: utf-8 -*-
import re
import random
with open('corpus1.txt','r') as f,open('82.txt','w') as g:
    for line in f:
        word_list = re.split(' ',line[:-1])
        for ind,word in enumerate(word_list):
            rand = random.randint(1,5)
            for i in range(-rand,rand+1):
                if ind+i >= 0 and ind+i < len(word_list) and word != word_list[ind+i]:
                    g.write(word+'\t'+word_list[ind+i]+'\n')
    g.close()
