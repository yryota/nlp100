# -*- coding: utf-8 -*-
import word2vec
import pickle
from collections import OrderedDict
word2vec.word2vec('corpus1.txt','corpus1.bin',size=300,verbose=True)
model = word2vec.load('corpus1.bin')
with open('90.pickle','wb') as f,open('d_t.pickle','wb') as g:
    pickle.dump(model.vectors,f)
    d_t = OrderedDict((word,i)for i,word in enumerate(model.vocab))
    pickle.dump(d_t,g)
