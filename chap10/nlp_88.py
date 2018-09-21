# -*- coding: utf-8 -*-
import numpy as np
import pickle
with open('90.pickle','rb') as f,open('d_t.pickle','rb') as g:
    X = pickle.load(f)
    d_t = pickle.load(g)
    v_eng = X[d_t['England'],:]
    cos_dict = {}
    for ti in d_t:
        if ti != 'England':
            v_word = X[d_t[ti],:]
            norm_ab = np.linalg.norm(v_word)*np.linalg.norm(v_eng)
            if norm_ab != 0:
                v_word = np.dot(v_word,v_eng)/norm_ab
            else:
                v_word = 0
            cos_dict.update({ti:v_word})
    cos_sort = sorted(cos_dict.items(),key=lambda x:x[1],reverse=True)
    for i,value in enumerate(cos_sort):
        if i >= 10:
            break
        print(value)
