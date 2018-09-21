# -*- coding: utf-8 -*-
import pickle
import numpy as np
def analyze(matrix,d_name,out):
    with open(matrix,'rb') as g,open(d_name,'rb') as d:
        m = pickle.load(g)
        d_t = pickle.load(d)
    with open('family.txt','r') as f,open(out,'w') as h:
        for line in f:
            word = line[:-1].split(' ')
            try:
                vec = m[d_t[word[1]],:]-m[d_t[word[0]],:]+m[d_t[word[2]],:]
            except:
                continue
            v_max = -1
            max_word = ''
            for k,v in d_t.items():
                v_tmp = m[v,:]
                norm_ab = np.linalg.norm(vec)*np.linalg.norm(v_tmp)
                if norm_ab != 0:
                    v_tmp = np.dot(v_tmp,vec)/norm_ab
                else:
                    v_tmp = 0
                if v_tmp > v_max:
                    v_max = v_tmp
                    max_word = k
            print(line[:-1]+' '+max_word+' '+str(v_max))
            h.write(line[:-1]+' '+max_word+' '+str(v_max)+'\n')

if __name__ == '__main__':
    analyze('90.pickle','d_t90.pickle','90out.txt')
    analyze('85.pickle','d_t.pickle','85out.txt')
