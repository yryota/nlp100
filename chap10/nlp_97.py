# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
import pickle
import numpy as np
import word2vec
model = word2vec.load('corpus1.bin')
with open('96.pickle','rb') as f,open('country_name.txt','r') as g:
    mat = pickle.load(f)
    km = KMeans(n_clusters=5)
    name = []
    pred = km.fit_predict(mat)
    for line in g:
        if ' ' in line:
            line = line.replace(' ','_')
        try:
            model[line[:-1]]
        except:
            continue
        name.append(line[:-1])
    n_dict = {}
    for i,n in enumerate(name):
        n_dict.update({n:pred[i]})
    print(sorted(n_dict.items(),key=lambda x:x[1]))
