"""Gabarito da Aula 12 - exercicios 1 a 4 (autocontido)."""
import numpy as np
from minisom import MiniSom
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits, load_iris, make_blobs
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import MinMaxScaler

print("Exercicio 1 (distancias)")
ponto = np.array([3.0, 4.0])
centros = np.array([[0.0, 0.0], [5.0, 5.0]])
d = np.linalg.norm(centros - ponto, axis=1)
print("distancias:", np.round(d, 2), "-> centroide", int(d.argmin()))

print("\nExercicio 2 (melhor k pela silhueta)")
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=1.2,
                  random_state=7)
for k in range(2, 7):
    km = KMeans(n_clusters=k, n_init=10, random_state=0).fit(X)
    print(k, round(silhouette_score(X, km.labels_), 3))

print("\nExercicio 3 (PCA nos digitos)")
Xd = load_digits().data / 16.0
acum = np.cumsum(PCA().fit(Xd).explained_variance_ratio_)
print("99% da variancia:", int(np.argmax(acum >= 0.99)) + 1, "componentes")

print("\nExercicio 4 (tamanho do mapa SOM)")
Xi = MinMaxScaler().fit_transform(load_iris().data)
for n in (3, 8):
    som = MiniSom(n, n, 4, sigma=1.5, learning_rate=0.5, random_seed=0)
    som.train_random(Xi, 3000)
    print(f"{n}x{n}: quantizacao", round(som.quantization_error(Xi), 3),
          " topografico", round(som.topographic_error(Xi), 3))
