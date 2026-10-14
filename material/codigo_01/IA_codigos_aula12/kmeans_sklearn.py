from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0,
                  random_state=42)
km = KMeans(n_clusters=3, n_init=10, random_state=0).fit(X)
print("inercia:", round(km.inertia_, 1))
print("iteracoes:", km.n_iter_)
print("centroides:\n", km.cluster_centers_.round(2))
print("tamanhos:", [int((km.labels_ == j).sum()) for j in range(3)])
ari = adjusted_rand_score(y, km.labels_)
print("ARI contra os grupos reais:", round(ari, 3))
print("novo ponto (0, 0) ->", int(km.predict([[0, 0]])[0]))
