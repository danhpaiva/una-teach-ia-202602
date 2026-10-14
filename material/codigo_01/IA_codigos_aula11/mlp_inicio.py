import numpy as np
from mlp_zero import treinar, forward

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

p0, h0 = treinar(X, y, zeros=True, epocas=3000)
s0 = np.round(forward(p0, X)[1].ravel(), 3)
print("zeros: perda", round(h0[-1], 4), s0)
print("W1 colunas iguais?", np.allclose(p0["W1"][:, 0], p0["W1"][:, 1]))
p1, h1 = treinar(X, y, zeros=False, epocas=3000)
s1 = np.round(forward(p1, X)[1].ravel(), 3)
print("aleatoria: perda", round(h1[-1], 4), s1)
