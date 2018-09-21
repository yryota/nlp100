# -*- coding: utf-8 -*-
import pickle
with open('90.pickle','rb') as f,open('d_t.pickle','rb') as g:
    X = pickle.load(f)
    d_t = pickle.load(g)
    print(X[d_t['United_States'],:])
