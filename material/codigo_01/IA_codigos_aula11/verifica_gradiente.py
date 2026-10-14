import numpy as np
from mlp_zero import iniciar, forward, perda, backward

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)
p = iniciar(2, 4, seed=0)
a1, a2 = forward(p, X)
g = backward(p, X, y, a1, a2)

h = 1e-6
for nome in ("W1", "W2"):
    i = (0, 0)
    p[nome][i] += h
    mais = perda(y, forward(p, X)[1])
    p[nome][i] -= 2 * h
    menos = perda(y, forward(p, X)[1])
    p[nome][i] += h
    num = (mais - menos) / (2 * h)
    print(nome, round(g[nome][i], 6), round(num, 6))
