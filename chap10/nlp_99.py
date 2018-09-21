# -*- codging: utf-8 -*-
from sklearn.manifold import TSNE
import pickle
import matplotlib.pyplot as plt
with open('96.pickle','rb') as f:
    mat = pickle.load(f)
    mat_reduce = TSNE(n_components=2,random_state=0).fit_transform(mat)
    plt.scatter(mat_reduce[:,0],mat_reduce[:,1])
    plt.show()
