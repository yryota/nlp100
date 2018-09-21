# -*- coding: utf-8 -*-
import scipy.cluster.hierarchy
import pickle
import matplotlib.pyplot as plt
with open('96.pickle','rb') as f:
    mat = pickle.load(f)
    res = scipy.cluster.hierarchy.ward(mat)
    d = scipy.cluster.hierarchy.dendrogram(res,leaf_font_size=8)
    plt.show()
