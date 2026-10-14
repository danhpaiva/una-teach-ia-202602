import numpy as np

X = np.array([[1.0, 1.0], [1.5, 2.0], [3.0, 4.0],
              [5.0, 7.0], [3.5, 5.0], [4.5, 5.0]])
c = np.array([[1.0, 1.0], [5.0, 7.0]])      # centroides iniciais

for it in range(1, 4):
    d = np.linalg.norm(X[:, None, :] - c[None, :, :], axis=2)
    rotulos = d.argmin(axis=1)
    if it == 1:
        print("distancias (iteracao 1):\n", np.round(d, 2))
    novos = np.array([X[rotulos == k].mean(axis=0) for k in range(2)])
    print("iteracao", it, "rotulos:", rotulos.tolist())
    print("  centroides:", np.round(novos, 2).tolist())
    if np.allclose(novos, c):
        print("  convergiu")
        break
    c = novos
