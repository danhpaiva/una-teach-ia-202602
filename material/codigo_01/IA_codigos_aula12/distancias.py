import numpy as np

a = np.array([1.0, 2.0])
b = np.array([4.0, 6.0])
print("diferenca:", b - a)
print("distancia euclidiana:", np.sqrt(np.sum((a - b) ** 2)))
print("com np.linalg.norm  :", np.linalg.norm(a - b))

pontos = np.array([[1.0, 1.0], [1.5, 2.0], [8.0, 8.0], [9.0, 9.5]])
centro = np.array([1.0, 1.0])
d = np.linalg.norm(pontos - centro, axis=1)
print("distancias:", np.round(d, 2))
