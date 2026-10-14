from sklearn.datasets import make_moons
from sklearn.cluster import KMeans, DBSCAN
from sklearn.metrics import adjusted_rand_score

X, y = make_moons(n_samples=300, noise=0.06, random_state=0)
km = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X)
db = DBSCAN(eps=0.2, min_samples=5).fit(X)
print("K-means ARI:", round(adjusted_rand_score(y, km.labels_), 3))
print("DBSCAN  ARI:", round(adjusted_rand_score(y, db.labels_), 3))
print("DBSCAN grupos:", sorted(int(g) for g in set(db.labels_) - {-1}),
      " ruido:", int((db.labels_ == -1).sum()))
