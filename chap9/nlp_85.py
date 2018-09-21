# -*- coding: utf-8 -*-
from scipy.sparse import lil_matrix
from sklearn.decomposition import TruncatedSVD
import pickle
with open('84.pickle','rb') as f,open('85.pickle','wb') as g:
    X = pickle.load(f)
    pca = TruncatedSVD(algorithm='arpack',n_components=300)
    pca.fit(X)
    X = pca.transform(X)
    pickle.dump(X,g)
