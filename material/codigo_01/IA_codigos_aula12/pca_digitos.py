import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

digitos = load_digits()
X = digitos.data / 16.0
y = digitos.target
pca = PCA().fit(X)
acum = np.cumsum(pca.explained_variance_ratio_)
for alvo in (0.80, 0.90, 0.95):
    n = int(np.argmax(acum >= alvo)) + 1
    print(int(alvo * 100), "% da variancia:", n, "componentes")

km = KMeans(n_clusters=10, n_init=10, random_state=0)
ari64 = adjusted_rand_score(y, km.fit(X).labels_)
print("K-means nos 64 pixels, ARI:", round(ari64, 3))
Z = PCA(n_components=20).fit_transform(X)
ari20 = adjusted_rand_score(y, km.fit(Z).labels_)
print("K-means em 20 componentes, ARI:", round(ari20, 3))
