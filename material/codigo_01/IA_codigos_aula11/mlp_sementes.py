import numpy as np
from mlp_zero import treinar, forward

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

for n_oc in (1, 2, 4):
    ok = 0
    for seed in range(20):
        p, h = treinar(X, y, n_oc=n_oc, epocas=3000, seed=seed)
        ok += (((forward(p, X)[1] > 0.5) == y).all())
    print(n_oc, "neuronios ocultos:", ok, "de 20 sementes")
