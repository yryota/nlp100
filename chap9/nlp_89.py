# -*- coding: utf-8 -*-
import pickle
import numpy as np
with open('85.pickle','rb') as f,open('d_t.pickle','rb') as g:
    X = pickle.load(f)
    d_t = pickle.load(g)
    v_spa = X[d_t['Spain'],:]
    v_mad = X[d_t['Madrid'],:]
    v_ath = X[d_t['Athens'],:]
    v = v_spa-v_mad+v_ath
    cos_dict = {}
    for ti in d_t:
        v_tmp = X[d_t[ti],:]
        norm_ab = np.linalg.norm(v)*np.linalg.norm(v_tmp)
        if norm_ab != 0:
            v_tmp = np.dot(v_tmp,v)/norm_ab
        else:
            v_tmp = 0
        cos_dict.update({ti:v_tmp})
    cos_sort = sorted(cos_dict.items(),key=lambda x:x[1],reverse=True)
    for i,value in enumerate(cos_sort):
        if i >= 10:
            break
        print(value)
