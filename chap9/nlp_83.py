# -*- coding: utf-8 -*-
import pickle
tc = {}
t = {}
c = {}
with open('82.txt','r') as f,open('83.pickle','wb') as g:
    cnt = 0
    for line in f:
        word = tuple(line[:-1].split('\t'))
        if word[0] in t.keys():
            t[word[0]] += 1
        else:
            t.update({word[0]:1})
        if word[1] in c.keys():
            c[word[1]] += 1
        else:
            c.update({word[1]:1})
        if word in tc.keys():
            tc[word] += 1
        else:
            tc.update({word:1})
        cnt += 1
    res = [cnt,tc,t,c]
    pickle.dump(res,g)

