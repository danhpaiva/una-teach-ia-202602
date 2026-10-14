import numpy as np
from mlp_zero import treinar, forward

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

for alfa in [0.01, 0.1, 0.5, 1.0, 5.0]:
    p, h = treinar(X, y, alfa=alfa, epocas=3000)
    acertos = ((forward(p, X)[1] > 0.5) == y).sum()
    print(f"alfa={alfa:5}: perda final={h[-1]:.4f}  acertos={acertos}/4")
