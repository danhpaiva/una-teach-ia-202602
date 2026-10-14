import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.preprocessing import StandardScaler

rng = np.random.default_rng(0)
idade = np.concatenate([rng.normal(25, 3, 100), rng.normal(50, 3, 100)])
renda = rng.normal(3000, 500, 200)
X = np.column_stack([idade, renda])
real = np.array([0] * 100 + [1] * 100)       # os grupos diferem pela idade

sem = KMeans(n_clusters=2, n_init=10, random_state=0).fit(X)
Xe = StandardScaler().fit_transform(X)
com = KMeans(n_clusters=2, n_init=10, random_state=0).fit(Xe)
print("ARI sem escala:", round(adjusted_rand_score(real, sem.labels_), 3))
print("ARI com escala:", round(adjusted_rand_score(real, com.labels_), 3))
