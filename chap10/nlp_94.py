# -*- coding: utf-8 -*-
import pickle
import numpy as np
def sim(pname,dname,out):
    with open('combined.tab','r') as f,open(pname,'rb') as g,open(dname,'rb') as h,open(out,'w') as d:
        mat = pickle.load(g)
        d_t = pickle.load(h)
        for line in f:
            word = line[:-1].split('\t')
            try:
                vec_a = mat[d_t[word[0]],:]
                vec_b = mat[d_t[word[1]],:]
            except:
                continue
            norm_ab = np.linalg.norm(vec_a)*np.linalg.norm(vec_b)
            if norm_ab != 0:
                vec_a = np.dot(vec_a,vec_b)/norm_ab
            else:
                vec_a = 0
            d.write(line[:-1]+'\t'+str(vec_a)+'\n')

if __name__ == '__main__':
    sim('85.pickle','d_t.pickle','85sim.txt')
    sim('90.pickle','d_t90.pickle','90sim.txt')
