# -*- coding: utf-8 -*-
import pickle
import math
from collections import OrderedDict
from scipy.sparse import lil_matrix,csr_matrix
with open('83.pickle','rb') as f,open('84.pickle','wb') as g,open('d_t.pickle','wb') as h,open('d_c.pickle','wb') as e:
    l = pickle.load(f)
    N = l[0]
    cnt = 0
    d_t = OrderedDict((key,i)for i,key in enumerate(l[2].keys()))
    d_c = OrderedDict((key,i)for i,key in enumerate(l[3].keys()))
    X = lil_matrix((len(d_t),len(d_c)))
    for tc_k,tc_v in l[1].items():
        cnt += 1
        if tc_v >= 10:
            print(tc_k,tc_v)
            print(str(cnt)+'/'+str(len(l[1])))
            t_v = tc_k[0]
            c_v = tc_k[1]
            X[d_t[t_v],d_c[c_v]] = max(math.log((N*tc_v)/(l[2][t_v]*l[3][c_v])),0)
    pickle.dump(X,g)
    pickle.dump(d_t,h)
    pickle.dump(d_c,e)
