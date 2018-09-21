# -*- coding: utf-8 -*-
import word2vec
import pickle
import numpy as np
import re
model = word2vec.load('corpus1.bin')
with open('country_name.txt','r') as f,open('96.pickle','wb') as g:
    mat = np.empty((0,300))
    for line in f:
        if ' ' in line:
            line = line.replace(' ','_')
        try:
            mat = np.r_[mat,model[line[:-1]].reshape(1,-1)]
        except:
            pass
    print(mat)
    pickle.dump(mat,g)
