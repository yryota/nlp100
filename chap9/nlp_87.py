# -*- coding: utf-8 -*-
import pickle
import numpy as np
with open('85.pickle','rb') as f,open('d_t.pickle','rb') as g:
    X = pickle.load(f)
    d_t = pickle.load(g)
    v_US = X[d_t['U.S'],:]
    v_us = X[d_t['United_States'],:]
    norm_ab = np.linalg.norm(v_US)*np.linalg.norm(v_us)
    if norm_ab != 0:
        cos = np.dot(v_US,v_us)/norm_ab
    else:
        cos = 0
    print(cos)
