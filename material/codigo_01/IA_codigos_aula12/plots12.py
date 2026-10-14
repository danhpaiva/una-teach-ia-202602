import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.cluster import KMeans, DBSCAN
from sklearn.datasets import make_blobs, make_moons, load_iris, load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler

COR = ["#0B8A5B", "#FF7A2F", "#D6336C", "#5B6EE1"]

# 1) blobs + K-means
X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
ax[0].scatter(X[:, 0], X[:, 1], s=14, c="#55645B")
ax[0].set_title("Dados sem rotulo", fontsize=13)
for j in range(3):
    ax[1].scatter(X[km.labels_ == j, 0], X[km.labels_ == j, 1], s=14, c=COR[j])
ax[1].scatter(*km.cluster_centers_.T, marker="X", s=180, c="black", edgecolor="white")
ax[1].set_title("K-means, k = 3 (X = centroides)", fontsize=13)
plt.tight_layout(); plt.savefig("blobs.png", dpi=150); plt.close()

# 2) elbow + silhouette -> json
from sklearn.metrics import silhouette_score
ine, sil = [], []
for k in range(1, 9):
    m = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    ine.append(round(float(m.inertia_), 1))
    sil.append(round(float(silhouette_score(X, m.labels_)), 3) if k > 1 else None)
json.dump({"inercia": ine, "silhueta": sil}, open("curvas12.json", "w"))

# 3) moons
Xm, ym = make_moons(n_samples=300, noise=0.06, random_state=0)
kmm = KMeans(n_clusters=2, n_init=10, random_state=0).fit(Xm)
db = DBSCAN(eps=0.2, min_samples=5).fit(Xm)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
for a, lab, t in ((ax[0], kmm.labels_, "K-means (k = 2)"), (ax[1], db.labels_, "DBSCAN (eps = 0,2)")):
    for j in sorted(set(lab)):
        a.scatter(Xm[lab == j, 0], Xm[lab == j, 1], s=14, c=COR[j % 4])
    a.set_title(t, fontsize=13)
plt.tight_layout(); plt.savefig("luas.png", dpi=150); plt.close()

# 4) SOM colors
rng = np.random.default_rng(0)
cores = rng.random((200, 3))
som = MiniSom(10, 10, 3, sigma=3.0, learning_rate=0.5, random_seed=0)
som.train_random(cores, 5000)
fig, ax = plt.subplots(1, 2, figsize=(8, 3.6))
ax[0].imshow(cores[:100].reshape(10, 10, 3)); ax[0].set_title("100 cores aleatorias", fontsize=13); ax[0].axis("off")
ax[1].imshow(som.get_weights()); ax[1].set_title("Mapa SOM 10x10 treinado", fontsize=13); ax[1].axis("off")
plt.tight_layout(); plt.savefig("som_cores.png", dpi=150); plt.close()

# 5) SOM iris u-matrix + classes
iris = load_iris(); Xi = MinMaxScaler().fit_transform(iris.data)
s2 = MiniSom(6, 6, 4, sigma=1.5, learning_rate=0.5, random_seed=0)
s2.train_random(Xi, 3000)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.9))
im = ax[0].pcolor(s2.distance_map().T, cmap="Greens"); ax[0].set_title("U-matrix (distancia entre vizinhos)", fontsize=12)
plt.colorbar(im, ax=ax[0])
ax[1].set_title("Classe de cada flor no mapa", fontsize=12)
for x, t in zip(Xi, iris.target):
    w = s2.winner(x)
    ax[1].scatter(w[0] + 0.5 + np.random.default_rng(int(sum(x*100))).uniform(-.3, .3),
                  w[1] + 0.5 + np.random.default_rng(int(sum(x*77))).uniform(-.3, .3), c=COR[t], s=14)
ax[1].set_xlim(0, 6); ax[1].set_ylim(0, 6); ax[1].grid(True, alpha=.3)
plt.tight_layout(); plt.savefig("som_iris.png", dpi=150); plt.close()

# 6) PCA iris
Xs = StandardScaler().fit_transform(iris.data)
Z = PCA(n_components=2).fit_transform(Xs)
fig, ax = plt.subplots(figsize=(5.2, 3.8))
for t, nome in enumerate(iris.target_names):
    ax.scatter(Z[iris.target == t, 0], Z[iris.target == t, 1], s=18, c=COR[t], label=nome)
ax.set_xlabel("componente 1 (73%)"); ax.set_ylabel("componente 2 (23%)"); ax.legend()
plt.tight_layout(); plt.savefig("pca_iris.png", dpi=150); plt.close()

# 7) PCA digits
dg = load_digits(); Xd = dg.data / 16.0
p = PCA(n_components=2).fit(Xd); Zd = p.transform(Xd)
fig, ax = plt.subplots(figsize=(5.2, 4.2))
sc = ax.scatter(Zd[:, 0], Zd[:, 1], c=dg.target, cmap="tab10", s=8)
plt.colorbar(sc, ax=ax, ticks=range(10))
ax.set_xlabel("componente 1"); ax.set_ylabel("componente 2")
plt.tight_layout(); plt.savefig("pca_digitos.png", dpi=150); plt.close()
full = PCA().fit(Xd); acum = np.cumsum(full.explained_variance_ratio_)
json.dump({"acum": [round(float(a), 3) for a in acum]}, open("pca_acum.json", "w"))
print("ok", round(float(p.explained_variance_ratio_.sum()), 3))
