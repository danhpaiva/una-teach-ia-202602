import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)            # y NAO e usado no treino
grupos = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(X)

for g in range(3):
    contagem = np.bincount(y[grupos == g], minlength=3)
    print("grupo", g, "-> especies reais (setosa, versicolor, virginica):", contagem)
