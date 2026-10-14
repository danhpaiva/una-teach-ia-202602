from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X, y = make_blobs(n_samples=300, centers=3, cluster_std=1.0,
                  random_state=42)
print("k  inercia  silhueta")
for k in range(1, 9):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    sil = silhouette_score(X, km.labels_) if k > 1 else float("nan")
    print(k, round(km.inertia_, 1), round(sil, 3))
