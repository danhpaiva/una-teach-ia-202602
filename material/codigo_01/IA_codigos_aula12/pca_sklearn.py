import numpy as np
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

X = load_iris().data
Xe = StandardScaler().fit_transform(X)
pca = PCA(n_components=2).fit(Xe)
print("variancia explicada:", np.round(pca.explained_variance_ratio_, 3))
print("soma:", round(float(pca.explained_variance_ratio_.sum()), 3))
print("componente 1:", np.round(pca.components_[0], 2))
print("componente 2:", np.round(pca.components_[1], 2))
Z = pca.transform(Xe)
back = pca.inverse_transform(Z)
print("erro de reconstrucao:", round(float(np.mean((Xe - back) ** 2)), 3))
