import numpy as np
from perceptron import Perceptron

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)

y = np.array([0, 0, 0, 1])          # AND
p = Perceptron(2, eta=0.1)
for ep in range(1, 8):
    erros = 0
    for xi, yi in zip(X, y):
        erro = yi - p.prever(xi)
        if erro != 0:
            p.w += p.eta * erro * xi
            p.b += p.eta * erro
            erros += 1
    print(f"epoca {ep}: w={np.round(p.w, 2)} b={p.b:.1f} erros={erros}")
    if erros == 0:
        break
