from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.2,
                  random_state=7)
for init in ("random", "k-means++"):
    inercias = []
    for seed in range(10):
        km = KMeans(n_clusters=4, init=init, n_init=1, random_state=seed)
        inercias.append(round(km.fit(X).inertia_, 1))
    print(init, "min", min(inercias), "max", max(inercias))
    print("  ", inercias)
