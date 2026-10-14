import numpy as np
from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import MinMaxScaler

iris = load_iris()
X = MinMaxScaler().fit_transform(iris.data)
som = MiniSom(6, 6, 4, sigma=1.5, learning_rate=0.5, random_seed=0)
print("erro de quantizacao antes :", round(som.quantization_error(X), 3))
som.train_random(X, 3000)
print("erro de quantizacao depois:", round(som.quantization_error(X), 3))
print("erro topografico:", round(som.topographic_error(X), 3))
print("vencedor da 1a flor:", tuple(int(v) for v in som.winner(X[0])))
print("pesos:", som.get_weights().shape)
